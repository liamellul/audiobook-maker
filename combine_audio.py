from pydub import AudioSegment
import os

# Get list of mp3 files in directory
files = [f for f in os.listdir('.') if f.endswith('.mp3')]
files.sort()  # Ensure files are in the correct order

# Concatenate audio files
combined = AudioSegment.empty()
for file in files:
    sound = AudioSegment.from_mp3(file)
    combined += sound

# Export as mp3
combined.export("combined.mp3", format='mp3')