import json


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    return len(text)


def analyze_text(text):
    result = {
        "text": text,
        "word_count": count_words(text),
        "character_count": count_characters(text),
    }

    return result


def save_analysis_to_json(analysis, filename="analysis_result.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(analysis, file, indent=4)


def main():
    user_text = input("Enter text to analyze: ")

    analysis = analyze_text(user_text)
    save_analysis_to_json(analysis)

    print("Analysis result:")
    print(f"Words: {analysis['word_count']}")
    print(f"Characters: {analysis['character_count']}")
    print("Result saved to analysis_result.json")


if __name__ == "__main__":
    main()