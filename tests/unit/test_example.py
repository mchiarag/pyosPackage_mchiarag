"""
A test module that tests your matcher module.

Some people prefer to write tests in a test file for each function or
method/class. Others prefer to write tests for each module. That decision
is up to you. This test example provides tests for the matcher.py module.
"""

from pyospackage_mchiarag.matcher import match_pokemon, get_available_words
import pytest


def test_match_pokemon_known_word():
    """
    Test that match_pokemon returns the correct Pokémon for a known word.

    A single line docstring for tests is generally sufficient.
    """
    out = match_pokemon("brave")
    expected_pokemon = "Charizard"
    assert out["pokemon"] == expected_pokemon, f"Expected {expected_pokemon} but got {out['pokemon']}"


def test_match_pokemon_unknown_word():
    """Test that match_pokemon returns None for an unknown word."""
    out = match_pokemon("banana")
    assert out is None, f"Expected None but got {out}"


def test_ten_words_available():
    """Test that there are exactly 10 personality words to choose from."""
    words = get_available_words()
    assert len(words) == 10, f"Expected 10 words but got {len(words)}"


def test_match_pokemon_raises_on_none():
    """match_pokemon should raise TypeError when given None."""
    with pytest.raises(TypeError, match="expects a string"):
        match_pokemon(None)


def test_match_pokemon_raises_on_integer():
    """match_pokemon should raise TypeError when given an integer."""
    with pytest.raises(TypeError, match="expects a string"):
        match_pokemon(42)


def test_match_pokemon_raises_on_list():
    """match_pokemon should raise TypeError when given a list."""
    with pytest.raises(TypeError, match="expects a string"):
        match_pokemon(["brave"])


import pytest


@pytest.mark.parametrize("bad_input", [None, 42, 3.14, [], {}, ("brave",), True])
def test_non_string_inputs_raise_typeerror(bad_input):
    """Any non-string input should raise TypeError."""
    with pytest.raises(TypeError):
        match_pokemon(bad_input)