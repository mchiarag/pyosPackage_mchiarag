"""Match personality words to famous Pokémon."""

POKEMON_MAP = {
    "brave":      {"pokemon": "Charizard",  "type": "Fire/Flying",    "reason": "A fearless dragon that soars into battle without hesitation!"},
    "loyal":      {"pokemon": "Pikachu",    "type": "Electric",       "reason": "The most loyal companion — sticks by its trainer through thick and thin!"},
    "mysterious": {"pokemon": "Mewtwo",     "type": "Psychic",        "reason": "A legendary being shrouded in secrets and raw psychic power."},
    "playful":    {"pokemon": "Jigglypuff", "type": "Normal/Fairy",   "reason": "Loves to sing and have fun — but don't fall asleep!"},
    "wise":       {"pokemon": "Alakazam",   "type": "Psychic",        "reason": "With an IQ over 5000, the embodiment of intelligence."},
    "strong":     {"pokemon": "Machamp",    "type": "Fighting",       "reason": "Four arms of pure power — you crush every challenge!"},
    "chill":      {"pokemon": "Snorlax",    "type": "Normal",         "reason": "The ultimate relaxation master. Good food + good nap = life."},
    "magical":    {"pokemon": "Gengar",     "type": "Ghost/Poison",   "reason": "Mischievous, otherworldly, full of surprises!"},
    "curious":    {"pokemon": "Eevee",      "type": "Normal",         "reason": "Full of potential, always evolving. Never the same twice!"},
    "fierce":     {"pokemon": "Dragonite",  "type": "Dragon/Flying",  "reason": "Gentle at heart, devastating in battle — a force of nature!"},
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
    print("\n🎮 Pick a word that describes you:\n")
    for i, w in enumerate(words, 1):
        print(f"  {i:>2}. {w}")

    choice = input("\n👉 Type a word: ").strip().lower()
    match = match_pokemon(choice)

    if not match:
        print(f"\n❌ '{choice}' isn't one of the words. Try again!")
        return

    print(f"\n✨ You are... {match['pokemon']}! ✨")
    print(f"🔰 Type: {match['type']}")
    print(f"💬 Why: {match['reason']}\n")