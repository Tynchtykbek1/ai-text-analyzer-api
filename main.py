def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    return len(text)


def analyze_text(text):
    result = {
        "word_count": count_words(text),
        "character_count": count_characters(text),
    }

    return result


def main():
    user_text = input("Enter text to analyze: ")

    analysis = analyze_text(user_text)

    print("Analysis result:")
    print(f"Words: {analysis['word_count']}")
    print(f"Characters: {analysis['character_count']}")


if __name__ == "__main__":
    main()