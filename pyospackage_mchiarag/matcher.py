"""Match personality words to Pokémon."""

POKEMON_MAP = {
    "brave":      {"pokemon": "Charizard",  "type": "Fire"},
    "loyal":      {"pokemon": "Pikachu",    "type": "Electric"},
    "mysterious": {"pokemon": "Mewtwo",     "type": "Psychic"},
    "playful":    {"pokemon": "Jigglypuff", "type": "Normal"},
    "wise":       {"pokemon": "Alakazam",   "type": "Psychic"},
    "strong":     {"pokemon": "Machamp",    "type": "Fighting"},
    "chill":      {"pokemon": "Snorlax",    "type": "Normal"},
    "magical":    {"pokemon": "Gengar",     "type": "Ghost"},
    "curious":    {"pokemon": "Eevee",      "type": "Normal"},
    "fierce":     {"pokemon": "Dragonite",  "type": "Dragon"},
}


def get_available_words():
    """Return the list of words a user can choose from."""
    return list(POKEMON_MAP.keys())


def match_pokemon(word):
    """Match a personality word to a Pokémon."""
    return POKEMON_MAP.get(word.strip().lower())


def pick_pokemon():
    """Prompt the user for a word and print their matching Pokémon."""
    words = get_available_words()
    print("\nPick a word that describes you best right now:\n")
    for i, w in enumerate(words, 1):
        print(f"  {i:>2}. {w}")

    choice = input("\nType a word: ").strip().lower()
    match = match_pokemon(choice)

    if not match:
        print(f"\n'{choice}' isn't one of the words. Try again!")
        return

    print(f"\nYou are {match['pokemon']}!")
    print(f"Type: {match['type']}")
    print(f"Consider adding this Pokèmon to your VS sidebar!")