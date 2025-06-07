
import  requests
import json
import pytest
from helperFunctions.taskHF import create_a_new_task #Import helper function
from helperFunctions.taskHF import create_task_payload #Import helper function


"""Test case: 1.Create a new task, 2.Get id of newly created task"""


#1.Create a new task
@pytest.mark.tc01 #Add Pytest marker
def test_create_new_task(): #Name test
    payload_create_task = create_task_payload() #Add create payload
    create_new_task_response = requests.put(create_a_new_task(), json=payload_create_task) #Send request to endpoint
    result_create_new_task_response = create_new_task_response.json() #Get response back as json
    pretty_print = json.dumps(result_create_new_task_response, indent=4) #Format response back
    assert create_new_task_response.status_code ==  200 #Assert status code
    print(pretty_print, create_new_task_response.status_code) #Print formatted response and status code


#2.Get ID of newly created task
    task_id = result_create_new_task_response["task"]["task_id"] #Get task_id for the task created
    assert task_id #Assert task_ID
    print(task_id)  # Print task_ID





