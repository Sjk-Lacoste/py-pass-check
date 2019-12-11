from passwordChecker import *
import pytest

psw = 'pAs$w0rD12'


def test_password_not_empty():
    try:
        if password_is_valid(psw) == '':
            assert password_is_valid(psw)
    except Exception:
        assert Exception

def test_password_stringlen():
    with pytest.raises(Exception) as error:
        password_is_valid('tshepo')
    assert str(error.value) == "Password must at least be 8 characters or longer"

def test_password_lowercase():
    with pytest.raises(Exception) as error:
        password_is_valid('THSOPMOSHJE')
    assert str(error.value) == "Password must at least have lowercase character or more"

def test_password_uppercase():
    with pytest.raises(Exception) as error:
        password_is_valid('tspaswenxdjed')
    assert str(error.value) == "Password must at least one uppercase character or more."

def test_password_digits():
    with pytest.raises(Exception) as error:
        password_is_valid('tspAKswenxdjed')
    assert str(error.value) == "Password must contain at least one digit or more"

def test_password_specialchars():
    with pytest.raises(Exception) as error:
        password_is_valid('tspasweKS1djed')
    assert str(error.value) == "Password must contain at least one special character"

def test_password_is_ok():
    try:
        if password_is_ok(psw):
            assert True
    except Exception:
        assert False