#import text analysis functions from stats.py
from stats import get_word_count, get_char_count, sorted_char_count

#read in book text from file
def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text

#main function to run the program. Prints report formatting. 
def main():
    
    #header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at /books/frankenstein.txt...")
    #word count
    print("----------- Word Count ----------")
    get_word_count(get_book_text("./books/frankenstein.txt"))
    print(get_word_count(get_book_text("./books/frankenstein.txt")))
    
    #character count
    print("--------- Character Count -------")
    book_char_count = get_char_count(get_book_text("./books/frankenstein.txt"))

    #sorted character count report
    alpha_char_count_report = sorted_char_count(book_char_count)

    #footer  
    print("============= END ===============")

main()
