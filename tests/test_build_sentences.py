import pytest
from build_sentences import (
    get_seven_letter_word, 
    parse_json_from_file, 
    choose_sentence_structure,
    get_pronoun, 
    get_article, 
    get_word, 
    fix_agreement, 
    build_sentence, 
    structures
)

def test_get_seven_letter_word(monkeypatch):
    # Test entering a valid word with 7+ letters
    monkeypatch.setattr('builtins.input', lambda _: "keyboard")
    assert get_seven_letter_word() == "KEYBOARD"

    # Test entering a short word (should raise ValueError)
    monkeypatch.setattr('builtins.input', lambda _: "cat")
    with pytest.raises(ValueError):
        get_seven_letter_word()

def test_parse_json_from_file():
    data = parse_json_from_file("word_lists.json")
    assert "nouns" in data
    assert "verbs" in data
    assert len(data["nouns"]) > 0

def test_choose_sentence_structure():
    assert choose_sentence_structure() in structures

def test_get_pronoun():
    assert get_pronoun() in ["he", "she", "they", "I", "we"]

def test_get_article():
    assert get_article() in ["a", "the"]

def test_get_word():
    # 'A' is index 0, 'B' is index 1, etc.
    test_words = ["apple", "banana", "cherry"]
    assert get_word("A", test_words) == "apple"
    assert get_word("B", test_words) == "banana"

def test_fix_agreement():
    # Rule 1: he/she adds 's' to verb 2 words ahead
    sentence = ["he", "happily", "run"]
    fix_agreement(sentence)
    assert sentence == ["he", "happily", "runs"]

    sentence = ["she", "always", "smile"]
    fix_agreement(sentence)
    assert sentence == ["she", "always", "smiles"]

    # Rule 2: 'a' becomes 'an' if noun 2 words ahead starts with a vowel
    sentence = ["a", "happy", "apple"]
    fix_agreement(sentence)
    assert sentence == ["an", "happy", "apple"]

    sentence = ["a", "happy", "dog"]
    fix_agreement(sentence)
    assert sentence == ["a", "happy", "dog"]

    # Rule 3: 'the' at index 0 adds 's' to verb 4 words later
    sentence = ["the", "cat", "happily", "run", "away"]
    fix_agreement(sentence)
    assert sentence == ["the", "cat", "happily", "run", "aways"]

def test_build_sentence():
    data = parse_json_from_file("word_lists.json")
    structure = structures[1]
    sentence = build_sentence("KEYBOARD", structure, data)
    
    assert sentence[0].isupper()
    assert len(sentence.split()) == len(structure)