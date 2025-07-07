from stats import get_book_text
from stats import count_char
from stats import dict_sorting

def main():
    path = "books/frankenstein.txt"
    book_in_string = get_book_text(path)
    list_string = book_in_string.split()
    word_count = len(list_string)
    #print(count_char(book_in_string))
    new_dict = count_char(book_in_string)
    sorted_list = dict_sorting(new_dict)
    del sorted_list[" "]
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")
    for i in sorted_list:
        print(f"{i}: {sorted_list[i]}")
    print("============= END ===============")

main()