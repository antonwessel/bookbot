def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_contents(book_path)
    book_words_count = count_words(book_text)
    characters_count = count_characters(book_text)
    print(characters_count)


def get_book_contents(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    book_list_length = len(text.split())
    return book_list_length


def count_characters(text):
    characters_count = {}
    for char in text:
        char = char.lower()
        if char in characters_count:
            characters_count[char] += 1
        else:
            characters_count[char] = 1
    return characters_count


if __name__ == "__main__":
    main()
