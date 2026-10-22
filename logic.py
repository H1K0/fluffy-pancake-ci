from storage import load_tasks, save_tasks


# Добавить задачу
def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)


# Получить список задач
def list_tasks():
    return load_tasks()


# Отметить задачу выполненной
def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        return True
    return False


# Удалить задачу
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
        return True
    return False
