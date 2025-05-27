#Imports
from stats import get_num_words
from stats import count_char
from stats import sort_dict
import sys

#Functions
def get_book_text(fpath):
    with open(fpath) as opfile:
        return opfile.read()
def main(argv):
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bPath = argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bPath}")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(bPath))}")
    print("--------- Character Count -------")

    #iterate through list and display alpha counts
    for x in sort_dict(count_char(get_book_text(bPath))):
        if x["char"].isalpha():
            print(f"{x["char"]}: {x["num"]}")


    print("============= END ===============")


#Start 
main(sys.argv)