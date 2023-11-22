# Specify the path to your text file
file_path = 'book.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the entire content of the file
    content = file.read()
    
    # Calculate the number of characters in the file
    num_characters = len(content)
    print(f"Number of characters: {num_characters}")

    # Calculate the cost for TTS API usage
    # The cost is calculated per 1000 characters
    tts_cost_per_1000_chars = 0.015  # Current TTS API cost per 1000 characters
    tts_cost = (num_characters / 1000) * tts_cost_per_1000_chars
    print(f"Estimated TTS API cost: ${tts_cost:.2f}")
