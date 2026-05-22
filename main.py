def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    return len(text)


def main():
    user_text = input("Enter text to analyze: ")

    word_count = count_words(user_text)
    character_count = count_characters(user_text)

    print("Analysis result:")
    print(f"Words: {word_count}")
    print(f"Characters: {character_count}")


if __name__ == "__main__":
    main()