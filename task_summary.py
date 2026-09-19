def summarize(tasks):
    total = len(tasks)
    done = sum(bool(task.get("done", False)) for task in tasks)
    return {"total": total, "done": done, "pending": total - done}


if __name__ == "__main__":
    tasks = [{"title": "Initialize repository", "done": True},
             {"title": "Add task summary", "done": False}]
    print(summarize(tasks))
