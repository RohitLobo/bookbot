from stats import get_book_word_count,get_char_count,sort_results
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents


    

def main():
    print(sys.argv)
    if len(sys.argv) < 2 or len(sys.argv)> 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...""")
    book_contents = get_book_text(sys.argv[1])
    word_count = get_book_word_count(book_contents)
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")
    char_count = (get_char_count(book_contents))
    results = sort_results(char_count) 
    for result in results:
        print(f"{result[0]}: {result[1]}")
    print("============= END ===============")
main()    