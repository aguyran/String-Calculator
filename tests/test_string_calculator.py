import pytest
from string_calculator import add


def test_empty():
    assert add("") == 0


def test_comma_newline():
    assert add("1") == 1
    assert add("1,2") == 3
    assert add("1\n2") == 3
    assert add("1\n2") == 3


def test_invalid_numbers():
    with pytest.raises(Exception) as excinfo:
        add("1,\n")
    assert str(excinfo.value) == "Invalid Number"


def test_custom_delimiter():
    assert add("//;\n1;2")
    assert add("//*\n2*3")


def test_negative_numbers():
    with pytest.raises(Exception) as excinfo:
        add("-1,-3")
    assert str(excinfo.value) == "negative numbers are not allowed -1,-3"

    with pytest.raises(Exception) as excinfo:
        add("//;\n-1;3")
    assert str(excinfo.value) == "negative numbers are not allowed -1"
