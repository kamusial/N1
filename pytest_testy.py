from pytest_funkcje import *

def test_dodawanie():
    assert dodawanie(4, 6) == 10

def test2_dodawanie():
    assert dodawanie(3, 3.5) == 7.5

def test3_dodawanie():
    assert dodawanie(4, 1) == 7

def test1_mnozenie():
    assert mnozenie (4, 60) == 240
def test2_mnozenie():
    assert mnozenie(100, 1.1) == 110
def test3_mnozenie():
    assert mnozenie(3, 3.5) == 10.5
def test4_mnozenie():
    assert mnozenie(3, 'mama') == 0