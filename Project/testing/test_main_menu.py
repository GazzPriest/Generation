from src.main_menu import main_menu_input
from pytest import MonkeyPatch

def test_main_menu_input_valid(monkeypatch: MonkeyPatch):
    input = ["3"]
    monkeypatch.setattr("builtins.input", lambda _: input.pop(0))
    main_menu_input()