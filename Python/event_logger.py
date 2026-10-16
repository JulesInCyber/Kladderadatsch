def event_logger(event, history=None):
    if history is None:
        history = []
        history.append(event)
    else:
        history.append(event)
    return history

print(event_logger("start"))
print(event_logger("stop", ["boot"]))
