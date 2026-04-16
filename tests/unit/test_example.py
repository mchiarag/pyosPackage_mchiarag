"""
A test module that tests your matcher module.

Some people prefer to write tests in a test file for each function or
method/class. Others prefer to write tests for each module. That decision
is up to you. This test example provides tests for the matcher.py module.
"""

from pyospackage_mchiarag.matcher import match_pokemon, get_available_words


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