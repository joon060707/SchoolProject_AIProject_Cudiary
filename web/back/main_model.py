# the ACTUAL model inference function for diagnosis process
# input: image path, plant id, plant name, date, description
# output: date, plant id, plant name, growth stage, organ type, diagnosis(disease), description(memo), image path
# input and output are json serializable dicts
# wait 3 seconds to simulate processing time
import time
import random
import sys
sys.path.append("../../models") # import module from parent directory
import viewclassifier_run as vc_run
import typeclassifier_run as tc_run
import greenness
import json
import datetime

def actual_diagnosis_model_inference(input_data: dict) -> dict:

    elapsed_time_start = time.time()


    # extract input data
    image_path = input_data.get("image_url", "")
    plant_id = input_data.get("plant_id", "")
    plant_name = input_data.get("plant_name", "Unknown Plant")
    date = input_data.get("datenow", "") # 2025-06-15 
    description = input_data.get("description", "")

    # use view classifier to determine organ type
    vc_result_json = vc_run.infer(image_path)
    vc_result = json.loads(vc_result_json) # contains predicted_class and confidence
    # "Whole plant", "Single organ"
    unit = vc_result["predicted_class"]
    unit_confidence = float(vc_result["confidence"])

    print(f"View Classifier: unit={unit} with confidence {unit_confidence}")
    elapsed_time_end = time.time()
    elapsed_time = elapsed_time_end - elapsed_time_start
    print(f"Elapsed time for view classification: {elapsed_time:.2f} seconds")



    # use type classifier to determine growth stage and diagnosis
    tc_result_json = tc_run.infer(image_path)
    tc_result = json.loads(tc_result_json) # contains predicted_class and confidence
    # "leaf", "flower", "fruit"
    organ_type = tc_result["predicted_class"]
    organ_type_confidence = float(tc_result["confidence"])

    print(f"Type Classifier: organ_type={organ_type} with confidence {organ_type_confidence}")
    elapsed_time_end2 = time.time()
    elapsed_time2 = elapsed_time_end2 - elapsed_time_end
    print(f"Elapsed time for type classification: {elapsed_time2:.2f} seconds")


    # calculate greenness index (ExG)
    greenness_index = greenness.calculate_greenness_index(image_path)
    print(f"Greenness Index: {greenness_index:.4f}")
    elapsed_time_end_greenness = time.time()
    elapsed_time_greenness = elapsed_time_end_greenness - elapsed_time_end2
    print(f"Elapsed time for greenness calculation: {elapsed_time_greenness:.2f} seconds")

    if greenness_index > 100:
        chlorophyll_content = "High"
    elif greenness_index > 60:
        chlorophyll_content = "Normal"
    else:
        chlorophyll_content = "Low"




    # there is a start date and current date for each plant, so we can determine the duration
    growth_start_date = input_data.get("growth_date", "") # date string #2025-05-01
    # day = growth duration in days
    day = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ") - datetime.datetime.strptime(growth_start_date, "%Y-%m-%d")
    print(f"Growth duration: {day.days} days")

    growth_stage = ""

    if day.days < 0:
        growth_stage = "Seedling"
        diagnosis = "Something was wrong."
        diagnosis_detail = "Please check the growth date."
    else:
        if unit == "Whole plant":
            growth_stage = "Vegetative"
            organ_type = "Leaf" # assume whole plant means leaf, but requires detection            
            diagnosis = "Healthy"
            diagnosis_detail = "You're looking at the whole plant(s). Please take a closer photo."

        elif organ_type == "Fruit":
            growth_stage = "Fruiting"
            # if > 60 days: too long to be harvested, maybe disease
            if day.days > 60:
                diagnosis = "Should be harvested"
                diagnosis_detail = "Check the fruit to avoid overripening or rot."
            else:
                diagnosis = "Healthy"
                diagnosis_detail = "Harvesting time is appropriate."
        elif organ_type == "Flower":
            growth_stage = "Flowering"
            # if < 20 days: too early, maybe disease
            if day.days < 20:
                diagnosis = "Too early flowering"
                diagnosis_detail = "Check the plant's environment conditions."
            else:
                diagnosis = "Healthy"
                diagnosis_detail = "No issues detected."
        elif organ_type == "Leaf":
            growth_stage = "Vegetative"
            # if > 30 days: too long, maybe disease
            if day.days > 30:            
                diagnosis = "Too late flowering"
                diagnosis_detail = "Check the plant's environment conditions."
            else:
                diagnosis = "Healthy"
                diagnosis_detail = "No issues detected."

    if(chlorophyll_content == "Low"):
        diagnosis = "Chlorophyll deficiency"
        diagnosis_detail = "Consider checking nutrient levels, water, and light exposure."

    
    elapsed_time_end3 = time.time()
    elapsed_time3 = elapsed_time_end3 - elapsed_time_end_greenness
    print(f"Elapsed time for rule-based diagnosis: {elapsed_time3:.2f} seconds")

    total_elapsed_time = elapsed_time_end3 - elapsed_time_start
    print(f"Total elapsed time for diagnosis inference: {total_elapsed_time:.2f} seconds")


    
    measurement = greenness_index # use greenness index as measurement for leaf


    # unit = random_choice("Whole plant", "Single organ")
    # organ_type = random_choice("Leaf", "Flower", "Fruit")
    # growth_stage = random_choice("Seedling", "Vegetative", "Flowering", "Fruiting")

    # diagnosis = random_choice("Healthy", "Disease A", "Disease B")
    # chlorophyll_content = random_choice("Normal", "Low", "High")

    # chlorophyll_content = "Normal" # placeholder


    # if organ_type == "Leaf" or organ_type == "Flower":
    #     measurement = greenness_index # use greenness index as measurement for leaf
    # else: # organ_type == "Fruit"
    #     measurement = random.randint(20, 30) # placeholder

    # measurement = "N/A"
    # diagnosis_detail = random_choice("No issues detected.", "Something was wrong.")


    # time.sleep(running_time)  # simulate processing time

    # construct output data
    output_data = {
        "date": date,
        "plant_id": plant_id,
        "plant_name": plant_name,

        "unit": unit,
        "unit_confidence": f"{unit_confidence:.4f}",
        "growth_stage": growth_stage,
        "organ_type": organ_type,
        "organ_type_confidence": f"{organ_type_confidence:.4f}",

        "diagnosis": diagnosis,
        "diagnosis_detail": diagnosis_detail,
        "chlorophyll_content": chlorophyll_content,
        "measurement": measurement,

        "description": description,
        "image_url": image_path+"_borders.png",

        "total_elapsed_time": total_elapsed_time
    }

    return output_data

# randomly return value from a list
def random_choice(*choices: list):
    return random.choice(choices)