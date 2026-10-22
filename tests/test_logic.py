import pytest

import logic


def test_list_is_empty_initially():
    assert logic.list_tasks() == []


def test_add_task():
    logic.add_task("Купить молоко")
    assert logic.list_tasks() == [{"title": "Купить молоко", "done": False}]


def test_mark_done_ok():
    logic.add_task("A")
    assert logic.mark_done(0) is True
    assert logic.list_tasks()[0]["done"] is True


@pytest.mark.parametrize("index", [-1, 0, 5])
def test_mark_done_bad_index(index):
    assert logic.mark_done(index) is False


def test_delete_task():
    logic.add_task("A")
    logic.add_task("B")
    assert logic.delete_task(0) is True
    assert [t["title"] for t in logic.list_tasks()] == ["B"]


def test_delete_task_bad_index():
    assert logic.delete_task(3) is False
