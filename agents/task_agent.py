def prioritize_tasks(tasks):
    return {
        "high": tasks[:1],
        "medium": tasks[1:]
    }