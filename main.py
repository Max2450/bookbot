#import sys to handle file paths using sys.argv
import sys

#import text analysis functions from stats.py
from stats import get_word_count, get_char_count, sorted_char_count

#read in book text from file
def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text

#main function to run the program. Prints report formatting. 
def main():

    if len(sys.argv) == 2:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    #header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    #word count
    print("----------- Word Count ----------")
    get_word_count(get_book_text(book_path))
    print(get_word_count(get_book_text(book_path)))
    
    #character count
    print("--------- Character Count -------")
    book_char_count = get_char_count(get_book_text(book_path))

    #sorted character count report
    alpha_char_count_report = sorted_char_count(book_char_count)

    #footer  
    print("============= END ===============")

main()
