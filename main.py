def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_contents(book_path)
    book_words_count = count_words(book_text)


def get_book_contents(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    book_list_length = len(text.split())
    return book_list_length


if __name__ == "__main__":
    main()
