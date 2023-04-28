def task_tracker(text): 
    if text is None:
        text = ""
        return "error"   
    elif "#TODO" in text:
        splittedText = text.split("#TODO")
        numTasks = len(splittedText) - 1 
        return f"You have {numTasks} task(s): \n -{splittedText[1:]}"
    else:
        return "You either do not not have any tasks or entered an empty string"