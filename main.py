def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
        return book_text

def get_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return f"{word_count} words found in the document"


def main():
    #print(get_book_text("./books/frankenstein.txt"))
    get_word_count(get_book_text("./books/frankenstein.txt"))
    print(get_word_count(get_book_text("./books/frankenstein.txt")))

main()
