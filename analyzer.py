def count_words(text):
    words = text.split()
    return len(words)


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

    if len(words) == 0:
        return 0

    total_length = 0

    for word in words:
        total_length += len(word)

    average = total_length / len(words)
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