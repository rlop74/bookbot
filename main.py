def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_list = sort_on(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    print(f"{sorted_list}")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    sorted_chars = sorted(chars.items(), key=lambda item: item[1], reverse=True)
    return sorted_chars

def sort_on(chars_dict):
    for item in chars_dict:
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
