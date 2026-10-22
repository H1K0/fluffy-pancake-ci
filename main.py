from logic import add_task, list_tasks, mark_done


def show():
    """Показать список задач с отметками о выполнении."""
    tasks = list_tasks()
    if not tasks:
        print("Список пуст.")
        return
    for i, t in enumerate(tasks):
        mark = "✔" if t["done"] else " "
        print(f"{i}. [{mark}] {t['title']}")


def main():
    """Точка входа: цикл меню с вводом команд."""
    while True:
        print("\n1) Добавить  2) Показать  3) Отметить  4) Выход")
        choice = input("> ").strip()

        if choice == "1":
            add_task(input("Название: "))
        elif choice == "2":
            show()
        elif choice == "3":
            show()
            try:
                mark_done(int(input("Номер: ")))
            except ValueError:
                print("Нужно число.")
        elif choice == "4":
            break
        else:
            print("Не понял команду.")


# Передаем управление в main при запуске программы
if __name__ == "__main__":
    main()
