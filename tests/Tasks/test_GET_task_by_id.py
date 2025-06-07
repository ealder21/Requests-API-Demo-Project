
import  requests
import json
import pytest
from helperFunctions.taskHF import create_a_new_task #Import helper function
from helperFunctions.taskHF import create_task_payload #Import helper function
from helperFunctions.taskHF import get_task_by_id #Import helper function


"""Test case: 1.Create a new task, 2.Get id of newly created task, 3. Get task by ID"""


#1.Create a new task
@pytest.mark.tc02 #Add Pytest marker
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


#3.Get task by the ID
    get_task_by_id_response = requests.get(f"{get_task_by_id()}/{task_id}") #Add the taskID as part of the path. Take note of the f string
    result_get_task_by_id_response =get_task_by_id_response.json() #Get response back as json
    pretty_print = json.dumps(result_get_task_by_id_response, indent=4) #Format response back
    assert get_task_by_id_response.status_code == 200 #Assert status code
    print(pretty_print,get_task_by_id_response.status_code) #Print formatted response and status code


    #Verify data in the response is correct
    verify_response_data = result_get_task_by_id_response #Store response in a variable
    assert verify_response_data["task_id"] == task_id #Assert task_id match what's in the response
    assert verify_response_data["content"] == payload_create_task["content"] #Assrt content matches what's in response
    print(verify_response_data) #Print verified data