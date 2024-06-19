import openai
from dotenv import find_dotenv, load_dotenv
import time
import logging
import json
from datetime import datetime

load_dotenv()


client = openai.OpenAI()
model = "gpt-4o"

filesObjs = client.files.list()

print(filesObjs)

for fileObj in filesObjs:
    file = client.files.delete(fileObj.id)
    print(f"Deleting: {fileObj.filename}; id: {fileObj.id}")
    
    
print ('Completed')