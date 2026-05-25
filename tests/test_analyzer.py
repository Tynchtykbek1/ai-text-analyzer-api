from analyzer import (
    analyze_text,
    count_words,
    count_characters,
    count_sentences,
    calculate_average_word_length,
)


def test_count_words():
    text = "Python, APIs, and real projects!"
    assert count_words(text) == 5


def test_count_characters():
    text = "AI"
    assert count_characters(text) == 2


def test_count_sentences():
    text = "AI is useful. Python is important! Is this clear?"
    assert count_sentences(text) == 3


def test_average_word_length():
    text = "Python APIs"
    assert calculate_average_word_length(text) == 5.0


def test_analyze_text_returns_dictionary():
    text = "AI engineering is practical."
    result = analyze_text(text)

    assert result["text"] == text
    assert result["word_count"] == 4
    assert result["sentence_count"] == 1
    assert "character_count" in result
    assert "average_word_length" in result