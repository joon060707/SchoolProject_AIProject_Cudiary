# the placeholder model for the diagnosis process
# input: image path, plant id, plant name, date, description
# output: date, plant id, plant name, growth stage, organ type, diagnosis(disease), description(memo), image path
# input and output are json serializable dicts
# wait 3 seconds to simulate processing time
import time
import random

def placeholder_diagnosis_model_inference(input_data: dict, running_time: float) -> dict:
    # extract input data
    image_path = input_data.get("image_url", "")
    plant_id = input_data.get("plant_id", "")
    plant_name = input_data.get("plant_name", "Unknown Plant")
    date = input_data.get("datenow", "")
    description = input_data.get("description", "")

    # placeholder logic for diagnosis
    # randomly generate diagnosis results
    unit = random_choice("Whole plant", "Single organ")
    organ_type = random_choice("Leaf", "Stem", "Fruit")
    growth_stage = random_choice("Seedling", "Vegetative", "Flowering", "Fruiting")

    diagnosis = random_choice("Healthy", "Disease A", "Disease B")
    chlorophyll_content = random_choice("Normal", "Low", "High")
    measurement = random.randint(0, 100)
    diagnosis_detail = random_choice("No issues detected.", "Something was wrong.")

    time.sleep(running_time)  # simulate processing time

    # construct output data
    output_data = {
        "date": date,
        "plant_id": plant_id,
        "plant_name": plant_name,

        "unit": unit,
        "growth_stage": growth_stage,
        "organ_type": organ_type,

        "diagnosis": diagnosis,
        "diagnosis_detail": diagnosis_detail,
        "chlorophyll_content": chlorophyll_content,
        "measurement": measurement,

        "description": description,
        "image_url": image_path
    }

    return output_data

# randomly return value from a list
def random_choice(*choices: list):
    return random.choice(choices)