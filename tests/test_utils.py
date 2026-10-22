import re

import utils


def test_now_str_format():
    assert re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", utils.now_str())


def test_ask_int_retries_until_number(monkeypatch, capsys):
    answers = iter(["abc", "", "42"])
    monkeypatch.setattr("builtins.input", lambda _="": next(answers))
    assert utils.ask_int("n: ") == 42
    assert "Нужно число" in capsys.readouterr().out


def test_ask_int_default_on_empty(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _="": "")
    assert utils.ask_int("n: ", default=7) == 7


def test_confirm(monkeypatch):
    for raw, expected in [("y", True), ("Да", True), ("n", False), ("", False)]:
        monkeypatch.setattr("builtins.input", lambda _="", r=raw: r)
        assert utils.confirm("ok?") is expected
