def get_book_text(filepath):
    with open(filepath) as b:
        return b.read()
    

def count_char(book_string):
    lowercase_string = book_string.lower()
    char_count = {}
    for i in lowercase_string:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count
