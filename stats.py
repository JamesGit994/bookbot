def get_book_text(filepath):
    with open(filepath) as b:
        return b.read()
    

def count_char(book_string):
    lowercase_string = book_string.lower()
    char_count = {}
    for i in lowercase_string:
        if i.isalpha():
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1
    return char_count


def dict_sorting(char_dict):
    sorting_items_in_new_list = sorted(char_dict.items(), key=lambda x:x[1], reverse=True)
    changing_list_to_dict = dict(sorting_items_in_new_list)
    return changing_list_to_dict
