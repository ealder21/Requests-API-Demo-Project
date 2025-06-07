
import  requests
import json
import pytest
from helperFunctions.taskHF import create_a_new_task #Import helper function
from helperFunctions.taskHF import create_task_payload #Import helper function
from helperFunctions.taskHF import get_task_by_id #Import helper function
from helperFunctions.taskHF import update_task_by_id #Import helper function
from helperFunctions.taskHF import updated_create_task_payload


"""Test case: 1.Create a new task, 2.Get id of newly created task, 3. Get task by ID"""

#1.Create a new task
@pytest.mark.tc03 #Add Pytest marker
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

#
#3.Create update payload.
    """In the helper function as an argument we need the task Id, we don't want to change this as we want to use the one 
    created, so as an argument we can use the NONE keyword. In the code we need to refer to it but pass the original
     ID"""
    update_task_payload = updated_create_task_payload(task_id=task_id) # Add updated payload


#4.Update the task with new data
    updated_task_response = requests.put(update_task_by_id(), json=update_task_payload) # Send request to endpoint
    result_updated_task_response = updated_task_response.json() #Get response back as json
    pretty_print = json.dumps(result_updated_task_response, indent=4) #Format response back
    assert updated_task_response.status_code == 200 #Assert status code
    print(pretty_print, updated_task_response.status_code) #Print formatted response and status code


#5.Get updated task by the ID
    get_updated_task_by_id_response = requests.get(f"{get_task_by_id()}/{task_id}") # Send request to endpoint
    result_get_updated_task_by_id_response = get_updated_task_by_id_response.json() #Get response back as json
    pretty_print = json.dumps(result_get_updated_task_by_id_response, indent=4) #Format response back
    assert get_updated_task_by_id_response.status_code == 200 #Assert status code
    print(pretty_print,get_updated_task_by_id_response.status_code) #Print formatted response and status code





