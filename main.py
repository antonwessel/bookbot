def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)


def get_book_contents(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_characters(text):
    characters_count = {}
    for char in text.lower():
        if char.isalpha():
            characters_count[char] = characters_count.get(char, 0) + 1
    return characters_count


def print_report(book_path):
    book_text = get_book_contents(book_path)
    book_words_count = count_words(book_text)
    characters_count = count_characters(book_text)

    sorted_char_count = sorted(
        characters_count.items(), key=lambda item: item[1], reverse=True
    )

    print(f"Printing report of {book_path}...")
    print(f"{book_words_count} words found in the text\n")
    for char, count in sorted_char_count:
        print(f"{char} was found {count} times")
    print("/// End of report ///")


if __name__ == "__main__":
    main()
