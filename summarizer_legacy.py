import openai
import tiktoken


# ==== INSTRUCTIONS ====
# # You are a creating writer writing an engaging daily newsletter based on world events. Your task is to write an essay summarizing the daily events in a creative entertaining style based on the articles input. the essay length should be 500 words. Style should be humorous, sarcastic, conservative, business oriented.

# Replace with your OpenAI API key
api_key = "your_openai_api_key"

# Initialize OpenAI with your API key
openai.api_key = api_key

# Function to read the content of a text file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Read the long transcript from a text file
file_path = "path_to_your_text_file.txt"  # Replace with the path to your text file
long_transcript = read_text_file(file_path)

# Tokenizer for the specific model
tokenizer = tiktoken.encoding_for_model("gpt-4")  # Use the appropriate model

# Function to split text into chunks based on token limit
def split_text(text, max_tokens):
    tokens = tokenizer.encode(text)
    chunks = []
    while len(tokens) > max_tokens:
        chunk = tokens[:max_tokens]
        chunks.append(tokenizer.decode(chunk))
        tokens = tokens[max_tokens:]
    chunks.append(tokenizer.decode(tokens))
    return chunks

# Split the transcript into chunks
max_tokens_per_chunk = 2000  # Adjust based on your needs and model limit
chunks = split_text(long_transcript, max_tokens_per_chunk)

# Function to summarize a single chunk
def summarize_chunk(chunk):
    prompt = f"Please summarize the following text in a concise form:\n\n{chunk}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150  # Adjust the token limit as needed for summary
    )
    summary = response['choices'][0]['message']['content']
    return summary

# Summarize each chunk
summaries = [summarize_chunk(chunk) for chunk in chunks]

# Combine summaries into a final summary
final_summary = " ".join(summaries)
print("Final Summary:", final_summary)
