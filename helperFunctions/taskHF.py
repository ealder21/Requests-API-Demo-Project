
import config as config #Import config as it stores baseURL and endpoints
from faker import Faker #Import faker library to generate random data


# Helper functions

# create a new task
def create_a_new_task():
    return config.base_URL + config.create_task_endpoint #


# update task by id
def update_task_by_id():
    return config.base_URL + config.update_task_endpoint


# Get task by id
def get_task_by_id():
    return config.base_URL + config.task_id_endpoint


# DELETE a task
def delete_a_task():
    return config.base_URL + config.delete_task_endpoint


# Create user payload
fake = Faker()
def create_task_payload():
    payload = {
        "content": fake.word(),
        "user_id": fake.word(),
        "is_done": False

    }
    return payload


# Update a task by ID
def updated_create_task_payload(task_id=None):
    update_task_payload = {
        "task_id": task_id,
        "content": fake.word(),
        "is_done": True
    }
    return update_task_payload