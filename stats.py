#takes in book text as a string and returns word count
def get_word_count(book_text):
    words = book_text.split()
    word_count = len(words)
    return f"Found {word_count} total words"

#takes in book text as a string and returns a dictionary with character counts
def get_char_count(book_text):
    char_count = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char not in char_count:
            char_count[lower_char] = 1
        else:
            char_count[lower_char] += 1
    return char_count

#takes in character count dictionary and returns a sorted list of dictionaries with character and count
def sorted_char_count(char_count):
    sorted_report = []
    
    #create list of dictionaries from char_count dict
    for char, num in char_count.items():
        inner_dict = {}
        inner_dict['char'] = char
        inner_dict['num'] = num
        sorted_report.append(inner_dict)

    #sort list of dictionaries by 'num' key in descending order
    sorted_report.sort(reverse=True, key=lambda d: d['num'])
    
    for dict in sorted_report:
        if not dict['char'].isalpha():
            continue
        print(f"{dict['char']}: {dict['num']}")

    return sorted_report