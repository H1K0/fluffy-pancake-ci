import pytest

import storage


@pytest.fixture(autouse=True)
def tmp_storage(tmp_path, monkeypatch):
    """Каждый тест работает с отдельным временным tasks.json."""
    monkeypatch.setattr(storage, "FILE", str(tmp_path / "tasks.json"))
