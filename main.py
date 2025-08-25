from stats import get_word_count, get_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text

def main():
    #print(get_book_text("./books/frankenstein.txt"))
    get_word_count(get_book_text("./books/frankenstein.txt"))
    print(get_word_count(get_book_text("./books/frankenstein.txt")))
    book_char_count = get_char_count(get_book_text("./books/frankenstein.txt"))
    print(book_char_count)

main()
