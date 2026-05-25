import string

def clean_word(word):
    return word.strip(string.punctuation).lower()

def count_words(text):
    words = text.split()
    cleaned_words = []

    for word in words:
        cleaned_word = clean_word(word)

        if cleaned_word:
            cleaned_words.append(cleaned_word)

    return len(cleaned_words)

def count_characters(text):
    return len(text)


def count_sentences(text):
    sentence_endings = [".", "!", "?"]
    count = 0

    for character in text:
        if character in sentence_endings:
            count += 1

    return count


def calculate_average_word_length(text):
    words = text.split()
    cleaned_words = []

    for word in words:
        cleaned_word = clean_word(word)

        if cleaned_word:
            cleaned_words.append(cleaned_word)

    if len(cleaned_words) == 0:
        return 0

    total_length = 0

    for word in cleaned_words:
        total_length += len(word)

    average = total_length / len(cleaned_words)
    return round(average, 2)


def analyze_text(text):
    result = {
        "text": text,
        "word_count": count_words(text),
        "character_count": count_characters(text),
        "sentence_count": count_sentences(text),
        "average_word_length": calculate_average_word_length(text),
    }

    return result