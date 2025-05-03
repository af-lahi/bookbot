from stats import word_count,each_char_count,sorted_char_count
from sys import argv,exit

def main():
  if len(argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)
  
  book_path = argv[1]
  book_text = get_book_text(book_path)
  book_word_count = word_count(book_text)
  book_char_count = sorted_char_count(each_char_count(book_text))
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}....")
  print("----------- Word Count -----------")
  print(f"Found {book_word_count} total words")
  print("--------- Character Count ---------")
  for char_item in book_char_count:
    if(char_item['char'].isalpha()):
      print(f"{char_item['char']}: {char_item['count']}")
  print("============= END ===============")

def get_book_text(file_path=''):
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents

  
main()