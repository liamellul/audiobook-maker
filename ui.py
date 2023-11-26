import tkinter as tk
from tkinter import filedialog
import ebooklib
from ebooklib import epub
import bs4
import openai
from openai import OpenAI
import os
from pathlib import Path
import threading

# Extracts and returns text from an EPUB file.
def extract_text(epub_path):
    book = epub.read_epub(epub_path)  # Read the EPUB file.
    all_text = []
    for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        soup = bs4.BeautifulSoup(doc.content, features='html.parser')  # Parse HTML content.
        all_text.append(soup.get_text())  # Extract and append text content.
    return '\n'.join(all_text)  # Return concatenated text.

# Calculates and returns the number of characters and estimated cost for TTS conversion.
def calculate_cost(text):
    num_characters = len(text)  # Count characters in the text.
    tts_cost_per_1000_chars = 0.015  # Define cost rate per 1000 characters.
    tts_cost = (num_characters / 1000) * tts_cost_per_1000_chars  # Calculate total cost.
    return num_characters, tts_cost

# Updates the cost label in the GUI with the number of characters and estimated cost.
def update_cost_label(num_characters, tts_cost):
    cost_label.config(text=f"Characters: {num_characters}\nEstimated TTS API cost: ${tts_cost:.2f}")

# Slices the text into segments according to a maximum length.
def slice_text(text, max_length):
    segments = []
    while text:
        segment = text[:max_length].rsplit(' ', 1)[0]  # Split at the last space to avoid cutting words.
        segments.append(segment)
        text = text[len(segment):].lstrip()  # Remove processed segment from text.
    return segments

# Converts text segments to speech using the OpenAI API.
def convert_text_to_speech(text_segments, voice):
    client = OpenAI()  # Initialize OpenAI client.

    for i, segment in enumerate(text_segments):
        try:
            speech_file_path = Path(f"output_part_{i+1}.mp3")  # Define path for the output file.
            response = client.audio.speech.create(
              model="tts-1",
              voice="fable",
              input=segment
            )
            response.stream_to_file(speech_file_path)  # Stream the audio response to a file.
            print(f"Audio part {i+1} saved as output_part_{i+1}.mp3")
        except Exception as e:
            print(f"An error occurred in part {i+1}: {e}")  # Handle any exceptions during the conversion.

# Main function to create the audiobook.
def make_audiobook():
    max_length = 4096  # API limit for text segment length.
    text_segments = slice_text(extracted_text, max_length)  # Slice text into segments.
    convert_text_to_speech(text_segments, "fable")  # Convert each segment to speech.

# Opens a dialog for the user to select an EPUB file and processes it.
def select_epub():
    global extracted_text
    file_path = filedialog.askopenfilename(filetypes=[("EPUB files", "*.epub")])  # Open file dialog.
    if file_path:
        extracted_text = extract_text(file_path)  # Extract text from selected EPUB.
        num_characters, tts_cost = calculate_cost(extracted_text)  # Calculate cost for TTS conversion.
        update_cost_label(num_characters, tts_cost)  # Update the GUI label with the cost info.

# Starts the audiobook creation in a separate thread.
def make_audiobook_thread():
    thread = threading.Thread(target=make_audiobook)  # Create a new thread for making the audiobook.
    thread.start()  # Start the thread.

# Set up the GUI elements.
root = tk.Tk()
root.title("EPUB to Audiobook Converter")

select_button = tk.Button(root, text="Select EPUB", command=select_epub)  # Button to select an EPUB file.
select_button.pack(pady=10)

cost_label = tk.Label(root, text="Characters: 0\nEstimated TTS API cost: $0.00")  # Label to show cost details.
cost_label.pack(pady=10)

audiobook_button = tk.Button(root, text="Make Audiobook", command=make_audiobook_thread)  # Button to start audiobook creation.
audiobook_button.pack(pady=10)

root.mainloop()  # Start the tkinter GUI loop.
