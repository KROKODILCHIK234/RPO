import pytest
from string_utils.core import reverse_string, remove_vowels, char_count

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""

def test_remove_vowels():
    assert remove_vowels("hello world") == "hll wrld"
    assert remove_vowels("AEIOUaeiou") == ""
    assert remove_vowels("bcdfg") == "bcdfg"

def test_char_count():
    assert char_count("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert char_count("aabb") == {'a': 2, 'b': 2}
    assert char_count("") == {}
