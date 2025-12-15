import pymysql.cursors
from datetime import datetime

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'aip',
}

def get_db_connection() -> pymysql.connections.Connection:
    connection = pymysql.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database'],
        cursorclass=pymysql.cursors.DictCursor
        )

    return connection


# Diary-related functions
def get_all_diary_entries():
    with get_db_connection().cursor() as cursor:
        # select all entries + plant name from plant table
        cursor.execute("SELECT diary.*, plant.plant_name FROM diary LEFT JOIN plant ON diary.plant_id = plant.plant_id")
        # cursor.execute("SELECT * FROM diary")
        result = cursor.fetchall()
    return result

def get_diary_entry_by_id(entry_id):
    with get_db_connection().cursor() as cursor:
        cursor.execute("SELECT * FROM diary WHERE id=%s", (entry_id,))
        result = cursor.fetchone()
        if not result:
            return None
    return result


# Plant-related functions
def get_all_plant_entries():
    with get_db_connection().cursor() as cursor:
        cursor.execute("SELECT * FROM plant")
        result = cursor.fetchall()
    return result

def get_plant_entry_by_id(plant_id):
    with get_db_connection().cursor() as cursor:
        cursor.execute("SELECT * FROM plant WHERE plant_id=%s", (plant_id,))
        result = cursor.fetchone()
    return result

# plant id: start from 1, get new max plant id
def get_new_max_plant_id():
    with get_db_connection().cursor() as cursor:
        cursor.execute("SELECT MAX(plant_id) FROM plant")
        result = cursor.fetchone()
        max_id = result["MAX(plant_id)"]
        return max_id + 1 if max_id is not None else 1

# if new plant, add plant entry (plant_id, plant_name, last_stage, note, start_date) is needed, first_date is mysql datetime format string
def add_plant_entry(plant_id, plant_name, last_stage, note, start_date):
    with get_db_connection().cursor() as cursor:
        cursor.execute(
            "INSERT INTO plant (plant_id, plant_name, last_stage, note, start_date)"
            "VALUES (%s, %s, %s, %s, %s)",
            (plant_id, plant_name, last_stage, note, start_date)
        )
        connection = cursor.connection
        connection.commit()
        return cursor.lastrowid


# Add Diary Entry (id, date, plant_id, unit, stage, organ_type, diagnosis, diagnosis_detail, chlorophyll_content, measurement, note, note2, img_path)
def add_diary_entry(date, plant_id, unit, stage, organ_type, diagnosis, diagnosis_detail, chlorophyll_content, measurement, note, note2, img_path):
    with get_db_connection().cursor() as cursor:

        # first, get the current max id
        cursor.execute("SELECT MAX(id) FROM diary")
        max_id = cursor.fetchone()["MAX(id)"]
        new_id = max_id + 1 if max_id is not None else 1

        # then, insert the new entry
        # date is mysql datetime format string
        # 2025-11-04T13:26:17.490Z -> 2025-11-04 13:26:17
        print(date)
        date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")
        
        print(plant_id)

        cursor.execute(
            "INSERT INTO diary (id, date, plant_id, unit, stage, organ_type, diagnosis, diagnosis_detail, chlorophyll_content, measurement, note, note2, img)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (new_id, date, plant_id, unit, stage, organ_type, diagnosis, diagnosis_detail, chlorophyll_content, measurement, note, note2, img_path)
        )
        connection = cursor.connection
        connection.commit()
        return new_id

# remove diary entry by id
def remove_diary_entry(entry_id):
    with get_db_connection().cursor() as cursor:
        cursor.execute("DELETE FROM diary WHERE id=%s", (entry_id,))
        connection = cursor.connection
        connection.commit()
        return entry_id

# update diary entry by id
    # "plant_id": plant_id,
    # "plant_name": plant_name,
    # "diary_id": diary_id,
    # "unit": unit,
    # "organ_type": organ_type,
    # "growth_stage": growth_stage,
    # "note": note,
    # "diagnosis": Health,
    # "chlorophyll_content": Chlorophyll,
    # "measurement": Measurement
def update_diary_entry(plant_id, plant_name, diary_id, unit, stage, organ_type, diagnosis, chlorophyll_content, measurement, note):
    with get_db_connection().cursor() as cursor:

        cursor.execute(
            "UPDATE diary SET unit=%s, stage=%s, organ_type=%s, diagnosis=%s, chlorophyll_content=%s, measurement=%s, note=%s " \
            "WHERE id=%s",
            (unit, stage, organ_type, diagnosis, chlorophyll_content, measurement, note, diary_id)
        )

        # update plant name in plant table as well
        cursor.execute(
            "UPDATE plant SET plant_name=%s, note=%s WHERE plant_id=%s",
            (plant_name, note, plant_id)
        )

        connection = cursor.connection
        connection.commit()
        return diary_id





# template to initialize the database
# create the tables if they do not exist
def initialize_database():
    with get_db_connection().cursor() as cursor:
        # create plant table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS plant (
            plant_id INT PRIMARY KEY,
            plant_name VARCHAR(255),
            last_stage VARCHAR(255),
            note TEXT,
            start_date DATETIME
        )
        """)
        # create diary table
        cursor.execute("""
        CREATE TABLE diary (
            id INT PRIMARY KEY,
            date DATETIME,
            plant_id INT,
            unit VARCHAR(30),
            stage VARCHAR(30),
            organ_type VARCHAR(30),
            diagnosis VARCHAR(30),
            diagnosis_detail VARCHAR(511),
            chlorophyll_content VARCHAR(30),
            measurement INT,
            note VARCHAR(511),
            note2 VARCHAR(511),
            img VARCHAR(511),
            FOREIGN KEY (plant_id) REFERENCES plant(plant_id)
        )
        """)
        connection = cursor.connection
        connection.commit()