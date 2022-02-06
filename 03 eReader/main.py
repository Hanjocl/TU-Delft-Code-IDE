# 03 eReader

# Create a constant called 'PAGE_SIZE' with the value 15 (we assume that a page is 15-line long)
PAGE_SIZE = 25
# Create a constant BOOK_PATH with the value 'book.txt'
BOOK_PATH = "03 eReader\Book.txt"

BOOK_TITLE = "Les Misérables"

# Create 3 constants W, O and B for quick access to colour characters
W  = '\033[0m'  # white (normal)
O  = '\033[33m' # orange
B  = '\033[34m' # blue

def show_book_page(file, page_size, title, page_count):
    # Show 40 empty lines
    print("\n" * 40)
    # Show the page header "==== title -- Page page_count ===="
    print(f"{O}==== {title} -- Page {page_count} ===={W}")
    # For the number of lines per page

    for i in range(0, page_size, 1):
        # Read the next line from the book
        line_content = file.readline(page_size)
        if line_content.startswith("CHAPTER"):
            line_content = line_content.title()
        # Show the user the next line of the book
        print(i, ". ",line_content)
    
    # Ask the user 'For the next page, press ENTER:' and store the answer in 'action'
    action = input('For the next page, press ENTER: ')
    return action

def read_book(path, page_size, title):
    # Open the file BOOK_PATH in 'read' mode and keep it in the 'book' variable
    file_book = open(path, "r", encoding='utf-8')
    # Create a variable page_count with the value 1
    page_count = 1
    # For the number of lines per page
    action = show_book_page(file_book, page_size, title, page_count)
    # Increment page count
    page_count += 1
    # While user pressed ENTER (empty string)
    while action == "":
        # If the user pressed ENTER (empty string)
        if  action == "":
            action = show_book_page(file_book, page_size, title, page_count)
            # Increment page count
            page_count += 1 
    
    # Close the file book.txt
    file_book.close()

read_book(BOOK_PATH, PAGE_SIZE, BOOK_TITLE)







