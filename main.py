def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

from stats import get_word_count, get_char_count, sort_chars_by_count

import sys
def main():
    if len(sys.argv) !=2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    num_words = get_word_count(text)
    char_count = get_char_count(text)
    sorted_characters = sort_chars_by_count(char_count)

    print(f"Found {num_words} total words")

    for item in sorted_characters:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()

