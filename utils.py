from datetime import datetime


def now_str():
    """Текущее время в формате '2026-10-08 14:30'."""
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def ask_int(prompt, default=None):
    """Спрашивает число, пока не введут корректное. Пустой ввод -> default."""
    while True:
        raw = input(prompt).strip()
        if not raw and default is not None:
            return default
        try:
            return int(raw)
        except ValueError:
            print("Нужно число, попробуй ещё раз.")


def confirm(prompt):
    """Возвращает True/False по y/n."""
    return input(f"{prompt} (y/n): ").strip().lower() in ("y", "yes", "д", "да")
