import main


def test_full_cli_flow(monkeypatch, capsys):
    # добавить -> показать -> отметить №0 -> показать -> выход
    answers = iter(["1", "Купить хлеб", "2", "3", "0", "2", "4"])
    monkeypatch.setattr("builtins.input", lambda _="": next(answers))

    main.main()

    out = capsys.readouterr().out
    assert "0. [ ] Купить хлеб" in out
    assert "0. [✔] Купить хлеб" in out


def test_cli_rejects_non_number(monkeypatch, capsys):
    answers = iter(["3", "abc", "4"])
    monkeypatch.setattr("builtins.input", lambda _="": next(answers))

    main.main()

    assert "Нужно число." in capsys.readouterr().out
