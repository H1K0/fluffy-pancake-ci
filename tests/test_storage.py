import storage


def test_save_and_load_roundtrip():
    data = [{"title": "Задача №1", "done": True}]
    storage.save_tasks(data)
    assert storage.load_tasks() == data
