import random
import fastapi
import db
import pydantic
import placeholdermodel
import main_model

app = fastapi.FastAPI()

# Enable CORS middleware
from fastapi.middleware.cors import CORSMiddleware
origins = ["*", "http://localhost:3000", "http://localhost:5173", "http://localhost:8000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"message": "Hello World"}

'''
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def sample():
    return {'message': 'This is a test endpoint'}
'''


# Diary-related endpoints
@app.get("/diary")
def get_diary_entries():    
    print("Fetching all diary entries")
    entries = db.get_all_diary_entries()
    return {"result":"success", "len": len(entries), "data": entries}

@app.get("/diary/{entry_id}")
def get_diary_entry(entry_id: int):    
    print("Fetching diary entry with ID:", entry_id)
    entry = db.get_diary_entry_by_id(entry_id)
    if not entry:
        return {"result":"error", "message": "Entry not found"}
    return {"result":"success", "message": "Entry found", "data": entry}



# Plant-related endpoints
@app.get("/plant")
def get_plant_entries():
    entries = db.get_all_plant_entries()
    return {"result":"success", "len": len(entries), "data": entries}

@app.get("/plant/{plant_id}")
def get_plant_entry(plant_id: int):
    entry = db.get_plant_entry_by_id(plant_id)
    if not entry:
        return {"result":"error", "message": "Entry not found"}
    return {"result":"success", "message": "Entry found", "data": entry}



# Diagnosis endpoint
# This is necessary to parse the input json body
class DiagnosisInput(pydantic.BaseModel):
    plant_id: int
    plant_name: str
    growth_date: str
    datenow: str
    description: str
    image_url: str

@app.post("/diagnosis")
def diagnose_plant(body: DiagnosisInput):

    # {"plant_id": 4, "plant_name": "Unknown Plant 4413432", "growth_date": "2025-10-27", "datenow": "2025-11-06T12:09:18.436Z", "description": "asdr ", "image_url": "http://localhost:3000/upload/1762398554331-1762398554323captured_image.png"}
    # convert to dict
    input_data_dict = body.model_dump()
    print("Parsed input data dict:", input_data_dict)

    # pre-check
    input_data_dict['plant_name'] = input_data_dict['plant_name'] if len(input_data_dict['plant_name'])>0 else f"New Plant {input_data_dict['plant_id']}"
    input_data_dict['description'] = input_data_dict['description'] if len(input_data_dict['description'])>0 else f"No description provided for New Plant {input_data_dict['plant_id']}"
    
    # If the plant is new, add it to the database
    plant_entry = db.get_plant_entry_by_id(input_data_dict["plant_id"])   
    if not plant_entry or input_data_dict["plant_id"] == 0: # new plant

        input_data_dict["plant_id"] = db.get_new_max_plant_id()
        print(f"New plant detected. Assigned plant_id: {input_data_dict['plant_id']}")

        db.add_plant_entry(
            plant_id=input_data_dict['plant_id'],
            plant_name=input_data_dict['plant_name'],
            last_stage="Seedling",  # from placeholder model
            note=input_data_dict['description'],
            start_date=input_data_dict['growth_date']
        )

        # retrieve the newly added plant entry
        plant_entry = db.get_plant_entry_by_id(input_data_dict["plant_id"])   
        input_data_dict['plant_name'] = input_data_dict['plant_name'] if len(input_data_dict['plant_name'])>0 else f"New Plant {input_data_dict['plant_id']}"
        input_data_dict['description'] = input_data_dict['description'] if len(input_data_dict['description'])>0 else f"No description provided for New Plant {input_data_dict['plant_id']}"
    
    
    # if the plant's name or description is updated, update the plant entry
    if plant_entry['plant_name'] != input_data_dict['plant_name'] or plant_entry['note'] != input_data_dict['description']:
        with db.get_db_connection().cursor() as cursor:
            cursor.execute(
                "UPDATE plant SET plant_name=%s, note=%s WHERE plant_id=%s",
                (input_data_dict['plant_name'], input_data_dict['description'], input_data_dict['plant_id'])
            )
            connection = cursor.connection
            connection.commit()
            print(f"Updated plant entry for plant_id {input_data_dict['plant_id']}")
        
    # call the placeholder model
    # later this will be replaced with the actual model inference
    # output_data = placeholdermodel.placeholder_diagnosis_model_inference(input_data_dict, running_time=random.random()*3+2)  # simulate 2-5 seconds processing time
    output_data = main_model.actual_diagnosis_model_inference(input_data_dict)

    # if description is default, replace it with diagnosis detail
    if input_data_dict["description"].startswith("No description provided"):
        output_data["description"] = output_data["diagnosis_detail"]

    # save the diagnosis result to the database
    diary_id = db.add_diary_entry(
        date=output_data["date"],
        plant_id=output_data["plant_id"],

        unit=output_data["unit"],
        stage=output_data["growth_stage"],
        organ_type=output_data["organ_type"],

        diagnosis=output_data["diagnosis"],
        diagnosis_detail=output_data["diagnosis_detail"],
        chlorophyll_content=output_data["chlorophyll_content"],
        measurement=output_data["measurement"],

        note=output_data["description"],
        note2="temp",  # You can modify this as needed
        img_path=output_data["image_url"]
    )
    return {"result":"success", "id": diary_id, "data": output_data}


# remove diary entry
@app.post("/diary/{entry_id}")
def remove_diary_entry(entry_id: int):
    print("Removing diary entry with ID:", entry_id)
    db.remove_diary_entry(entry_id)
    print("Diary entry removed.")
    return {"result":"success", "message": "Entry removed"}


# update entry class
# valid fields
    # "diary_id": diary_id,
    # "unit": unit,
    # "organ_type": organ_type,
    # "growth_stage": growth_stage,
    # "note": note,
    # "diagnosis": Health,
    # "chlorophyll_content": Chlorophyll,
    # "measurement": Measurement
class UpdateDiagnosisInput(pydantic.BaseModel):
    plant_id: int
    plant_name: str
    diary_id: int
    unit: str
    organ_type: str
    growth_stage: str
    note: str
    diagnosis: str
    chlorophyll_content: str
    measurement: float


# update diary entry
@app.post("/diary/update/{entry_id}")
def update_diary_entry(entry_id: int, body: UpdateDiagnosisInput):
    print("Updating diary entry with ID:", entry_id)
    input_data_dict = body.model_dump()
    print("Parsed input data dict for update:", input_data_dict)

 # plant_id, plant_name, diary_id, unit, stage, organ_type, diagnosis, chlorophyll_content, measurement, note
    db.update_diary_entry(
        plant_id=input_data_dict["plant_id"],
        plant_name=input_data_dict["plant_name"],
        diary_id=entry_id,
        unit=input_data_dict["unit"],
        stage=input_data_dict["growth_stage"],
        organ_type=input_data_dict["organ_type"],
        diagnosis=input_data_dict["diagnosis"],
        chlorophyll_content=input_data_dict["chlorophyll_content"],
        measurement=input_data_dict["measurement"],
        note=input_data_dict["note"]
    )
    print("Diary entry updated.")
    return {"result":"success", "message": "Entry updated"}


class Remove(pydantic.BaseModel):
    diary_id: int

# remove diary entry by id
@app.post("/diary/remove/{entry_id}")
def remove_diary_entry(entry_id: int, body: Remove):
    print("Removing diary entry with ID:", body.diary_id)
    db.remove_diary_entry(body.diary_id)
    print("Diary entry removed.")
    return {"result":"success", "message": "Entry removed"}