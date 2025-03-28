import sys
from stats import get_num_words, get_char_count, convert_chardict_to_listofdict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])
    total_words = get_num_words(file_contents)
    total_chars = get_char_count(file_contents)
    total_chars_sorted = convert_chardict_to_listofdict(total_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for pair in total_chars_sorted:
        if pair["char"].isalpha():
            print(f'{pair["char"]}: {pair["num"]}')
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
