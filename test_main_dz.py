import pytest
from main_dz import count_vowels

def test_count_vowels():
    assert count_vowels('МаДмАзель') == 3

def test_count_vowels():
    assert count_vowels('МаДмАзель') == 3

def test_count_vowels():
    assert count_vowels('МаДмАзель') == 3

@pytest.mark.parametrize("word, expected", [
    ("hello", 2),                  # Слово с английскими гласными
    ("Привет", 2),                # Слово с русскими гласными
    ("Mixed text: привет", 5),    # Смешанный текст с английскими и русскими гласными
    ("No vowels", 3),             # Фраза с английскими гласными
    ("Только согласные", 6),      # Фраза с русскими гласными
])
def test_count_vowels_parametrize(word, expected):
    assert count_vowels(word) == expected
