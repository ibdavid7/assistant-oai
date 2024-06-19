import openai
from dotenv import find_dotenv, load_dotenv
import time
import logging
import json
from datetime import datetime, timedelta

load_dotenv()


client = openai.OpenAI()
model = "gpt-4o"


# Function to read the content of a text file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Read the long transcript from a text file
file_path = "./articles.txt"  # Replace with the path to your text file
long_transcript = read_text_file(file_path)


prompt = "You are a creating writer writing an engaging daily newsletter based on world events. Your task is to write an essay summarizing the daily events in a creative entertaining style based on the articles input. the essay length should be 700 words. Style should be humorous, sarcastic, conservative, business oriented. Make the paragraphs build on each other in logical sequence - this happened and therefore this happened, or this happened because that happened"

response = client.chat.completions.create(
    model=model,
    messages=[
    {"role": "user", "content": prompt},
    {"role": "user", "content": long_transcript},
    ],
    temperature=1.5,
    max_tokens=2000,
    top_p=0.8,
)

result = response.choices[0].message.content

# Write the result to a text file
output_file = 'result.txt'
with open(output_file, 'a', encoding='utf-8') as file:
    # Add a timestamp to the output
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"Timestamp: {timestamp}\n")
    # Append to the file
    file.write(result)

print(result)

