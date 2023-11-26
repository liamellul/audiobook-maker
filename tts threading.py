import os
import threading
from openai import OpenAI
from pathlib import Path

# Function to slice the text
def slice_text(file_path, max_length):
    with open(file_path, 'r') as file:
        text = file.read()

    segments = []
    while text:
        segment = text[:max_length].rsplit(' ', 1)[0]
        segments.append(segment)
        text = text[len(segment):].lstrip()

    return segments

def convert_segment_to_speech(client, segment, part_num):
    try:
        speech_file_path = Path(f"output_part_{part_num}.mp3")
        response = client.audio.speech.create(
            model="tts-1",
            voice="fable",
            input=segment
        )
        response.stream_to_file(speech_file_path)
        print(f"Audio part {part_num} saved as output_part_{part_num}.mp3")
    except Exception as e:
        print(f"An error occurred in part {part_num}: {e}")

# Function to convert text to speech using threading
def convert_text_to_speech(text_segments, voice):
    client = OpenAI()
    threads = []

    for i, segment in enumerate(text_segments):
        thread = threading.Thread(target=convert_segment_to_speech, args=(client, segment, i+1))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Main execution
file_path = 'book.txt'
max_length = 4096  # Set this based on the API limit
text_segments = slice_text(file_path, max_length)

# using "Fable" voice but you can select whichever 
convert_text_to_speech(text_segments, "fable")