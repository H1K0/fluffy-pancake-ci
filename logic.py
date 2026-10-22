from storage import load_tasks, save_tasks


def add_task(title):
    """Добавить задачу с названием `title` в список и сохранить."""
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)


def list_tasks():
    """Получить список всех задач."""
    return load_tasks()


def mark_done(index):
    """Отметить задачу с номером `index` выполненной.

    Возвращает True, если задача найдена, и False при неверном номере.
    """
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        return True
    return False


def delete_task(index):
    """Удалить задачу с номером `index`.

    Возвращает True, если задача удалена, и False при неверном номере.
    """
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
        return True
    return False
