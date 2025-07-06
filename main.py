def get_book_text(filepath):
    with open(filepath) as b:
        return b.read()
    

def main():
    path = "books/frankenstein.txt"
    book_in_string = get_book_text(path)
    list_string = book_in_string.split()
    word_count = len(list_string)
    print(f'{word_count} words found in the document')


main()