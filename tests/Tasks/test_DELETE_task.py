
import  requests
import json
import pytest
from helperFunctions.taskHF import create_task_payload
from helperFunctions.taskHF import get_task_by_id
from helperFunctions.taskHF import delete_a_task
from helperFunctions.taskHF import create_a_new_task


'''Test case:
1: create a new task, 
2: delete the task,
3: verify task has been deleted'''


#1.Create a new task
@pytest.mark.tc04
def test_delete_a_task():
    payload_create_task = create_task_payload()# Add create payload
    create_a_new_task_response = requests.put(create_a_new_task(), json=payload_create_task) #Send request to endpoint
    result_create_a_new_task_response = create_a_new_task_response.json() #Get response back as json
    pretty_print = json.dumps(result_create_a_new_task_response, indent=4) #Format response back
    assert create_a_new_task_response.status_code == 200 #Assert status code
    print(pretty_print, create_a_new_task_response.status_code) #Print formatted response and status code


#2.Get task ID
    task_id = result_create_a_new_task_response["task"]["task_id"] #Get task_id for the task created
    assert task_id
    print(task_id)


#3.Delete task
    delete_task_by_id_response = requests.delete(f"{delete_a_task()}/{task_id}") #Send request to endpoint
    result_delete_task_by_id_response = delete_task_by_id_response.json() #Get response back as json
    pretty_print = json.dumps(result_delete_task_by_id_response, indent=4) #Format response back
    assert delete_task_by_id_response.status_code == 404 #Assert status code
    print(pretty_print, delete_task_by_id_response.status_code) #Print formatted response and status code


#4.Try and get task deleted by ID
    get_deleted_task_by_id_response = requests.get(f"{get_task_by_id()}/{task_id}") #Send request to endpoint
    result_get_deleted_task_by_id_response = get_deleted_task_by_id_response.json() #Get response back as json
    pretty_print =json.dumps(result_get_deleted_task_by_id_response, indent=4) #Format response back
    assert get_deleted_task_by_id_response.status_code == 200 #Assert status code
    print(pretty_print, delete_task_by_id_response.status_code) #Print formatted response and status code





