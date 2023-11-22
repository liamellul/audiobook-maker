import ebooklib
from ebooklib import epub
import bs4

# Function to extract text from an EPUB file
def extract_text(epub_path):
    # Read the EPUB file
    book = epub.read_epub(epub_path)
    all_text = []

    # Loop through each document in the EPUB file
    for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        # Use BeautifulSoup to parse the HTML content
        soup = bs4.BeautifulSoup(doc.content, features='html.parser')
        # Extract and append the text to the list
        all_text.append(soup.get_text())

    # Join all extracted text into a single string
    return '\n'.join(all_text)

# Path to the EPUB file
epub_file_path = 'The Four Steps to the Epiphany.epub' # paste relative path here

# Extract text from the EPUB file
extracted_text = extract_text(epub_file_path)

# Path for the output text file
output_file_path = 'book.txt'

# Save the extracted text to the output file
with open(output_file_path, 'w') as file:
    file.write(extracted_text)
