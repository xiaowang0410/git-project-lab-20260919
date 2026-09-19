def summarize(tasks):
    return {"total": len(tasks)}


if __name__ == "__main__":
    tasks = [{"title": "Initialize repository", "done": True},
             {"title": "Add task summary", "done": False}]
    print(summarize(tasks))
