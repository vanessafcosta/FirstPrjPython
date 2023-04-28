from lib.task_tracker import *

"""
Given a text that do not contain any task. 
It returns that I do not have task. 
"""
def test_task_tracker_no_todo():
    result = task_tracker("This is an example without tasks.")
    assert result == "You either do not not have any tasks or entered an empty string"

def test_task_tracker_one_todo():
    result = task_tracker("#TODO Buy cheese for breakfast")
    assert result == "You have 1 task(s): \n -[' Buy cheese for breakfast']"


def test_task_tracker_more_one_todo():
    result = task_tracker("#TODO Buy cheese for breakfast #TODO Go to the bank to pick up card. ")
    assert result == "You have 2 task(s): \n -[' Buy cheese for breakfast ', ' Go to the bank to pick up card. ']"

def test_task_tracker_empty_string():
    result = task_tracker("")
    assert result == "You either do not not have any tasks or entered an empty string"

def test_task_tracker_empty_string():
    result = task_tracker(None)
    assert result == "error"