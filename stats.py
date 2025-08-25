def get_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return f"{word_count} words found in the document"

def get_char_count(book_text):
    char_count = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char not in char_count:
            char_count[lower_char] = 1
        else:
            char_count[lower_char] += 1
    return char_count