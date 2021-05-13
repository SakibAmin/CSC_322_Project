from db_connector import get_db_connection

def is_on_avoid_list(person_id):
    with get_db_connection() as conn:
        q_check_list = "SELECT EXISTS(SELECT * FROM avoid_list WHERE person_id={})".format(person_id)
        with conn.cursor() as cursor:
            cursor.execute(q_check_list)
            return cursor.fetchone()[0]

def notify_person(person_id):
    pass

def add_to_avoid_list(person_id, reason: str):
    with get_db_connection() as conn:
        q_add_person = "INSERT INTO avoid_list VALUES ({}, {})".format(person_id, reason)
        with conn.cursor() as cursor:
            cursor.execute(q_add_person)
        notify_person()

def avoid_reason(person_id):
    with get_db_connection() as conn:
        q_avoid_reason = "SELECT reason FROM avoid_list WHERE person_id={}".format(person_id)
        with conn.cursor() as cursor:
            cursor.execute(q_avoid_reason)
            print(cursor.fetchone()[0])
