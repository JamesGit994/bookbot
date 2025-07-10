import sys
from stats import get_book_text
from stats import count_char
from stats import dict_sorting

def main():
    try:
        if sys.argv[1]:
            path = sys.argv[1]
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_in_string = get_book_text(path)
    list_string = book_in_string.split()
    word_count = len(list_string)
    new_dict = count_char(book_in_string)
    sorted_list = dict_sorting(new_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")
    for i in sorted_list:
        print(f"{i}: {sorted_list[i]}")
    print("============= END ===============")

main()