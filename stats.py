def get_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return f"{word_count} words found in the document"