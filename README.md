### EPUB 2 AUDIOBOOK

This workflow below allows you to convert an EPUB into an Audiobook that is listenable using an OpenAI API key for the Whisper API.

The cost of Text-to-Speech (TTS) using [OpenAI's Whisper API](https://platform.openai.com/docs/guides/text-to-speech) at the time of writing for TTS-1 is $0.015 per 1K characters. The default for this code is "Fable" voice, there are others you can test at the link provided above.

To estimate the cost, analyze the number of characters in the text file by the API pricing. I have a script below that helps you with the character count.

### Example

Let's consider a text file with 176,216 characters.

1. Divide the total number of characters by 1,000. For example, 176,216 / 1,000 = 176.22.
2. Multiply the result by the cost per 1K characters. For example, 176.22 * $0.015 = $2.64.

Therefore, the estimated cost for this text file would be $2.64.

OpenAI API pricing as of writing is available here: https://openai.com/pricing please check this and don't take my word for it. I accept 0 liability if you YOLO your API keys.

### Files

#### epub2txt.py
- this script takes the .epub file specified in it's path and then converts it to a .txt file.

#### cost_estimator.py
- if you want a rough cost estimation this script takes the characters of the book.txt file and makes a guess, displaying total characters of the .txt file and also the price estimation.
- Please also check yourself, do not use this as a final confirmation. prices might change etc. I accept no liability at all. 
- It is still useful for determining how many characters will go to the API.

#### tts.py
- takes the .txt file "book.txt" in the project directory and sends chunks of ~5000 characters (max limit) to the whisper TTS API.

#### combine_audio.py
- stitches together all of the .mp3 files into a "combined.mp3".


### Licence

This code is distributed under MIT licence, see the LICENCE.md file for more information.