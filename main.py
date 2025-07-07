from stats import get_book_text
from stats import count_char

def main():
    path = "books/frankenstein.txt"
    book_in_string = get_book_text(path)
    list_string = book_in_string.split()
    word_count = len(list_string)
    print(f'{word_count} words found in the document')
    print(count_char(book_in_string))

main()