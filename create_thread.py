import openai
from dotenv import find_dotenv, load_dotenv
import time
import logging
import json
from datetime import datetime, timedelta


load_dotenv()
# openai.api_key = os.environ.get("OPENAI_API_KEY")
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )

client = openai.OpenAI()
model = "gpt-4o"


question_object = {
    "difficulty": "easy",
    "layout": "optionsOnly",
    "question_text": "Which cloud deployment model best describes AWS?",
    "score": 1,
    "answer": {
        "answer_image": "",
        "answer_text": "<p>AWS is primarily a public cloud deployment model where a user can provision resources in the public cloud. Resources are provisioned for open use by the general public, business, academic, government organizations, or some combination of them. Resources exist on the premises of the cloud provider.</p>",
        "values": [
            {
                "type": "option_id",
                "index": 0,
                "value": "2d59aae0-0148-4ef3-8181-33b31bb5c8f8"
            }
        ]
    },
    "label": "Cloud Concepts",
    "type": "multiple_answer_1",
    "question_id": "4275112b-dbab-4f6f-ac29-4dc48f250d4c",
    "answer_image": "null",
    "question_image": "null",
    "options": [
        {
            "option_id": "2d59aae0-0148-4ef3-8181-33b31bb5c8f8",
            "option_header": "Public Cloud",
            "option_text": "",
            "option_image": "null"
        },
        {
            "option_id": "958a9f13-2d6b-4334-ad6c-685fbf35a251",
            "option_header": "Private Cloud",
            "option_text": "",
            "option_image": "null"
        },
        {
            "option_id": "062a754e-3c24-45c8-bd0c-d44a9f2f0c76",
            "option_header": "Hybrid Cloud",
            "option_text": "",
            "option_image": "null"
        },
        {
            "option_id": "cf3cd67f-6880-4e76-b375-ca8adedfe349",
            "option_header": "Community Cloud",
            "option_text": "",
            "option_image": "null"
        }
    ]
}

# Calculate the expiry time 15 minutes from now
# expiry_time = datetime.now() + timedelta(minutes=15)

# # === Thread (uncomment this to create your Thread) ===
thread = client.beta.threads.create(
    messages=[
        {
            "role": "assistant", "content": "You are in JSON mode."
        },
        {
            "role": "user",
            "content": f'I\'m answering AWS practice exam and I would like further assistance with the question. Question context: {question_object}',
        },
        {
            "role": "assistant",
            "content": """Hey there! Quizby is now using the power of AI to help you study more effectively. Let's get started?\n
            What would you like to do next? Here are some options:\n
            1. Explain the question, each of the options, and answer the question (Explain question)\n
            2. Explain the concepts involved and provide examples (Explain Concept)\n
            3. Generate a practice exam question (Quiz Me)\n
            4. Be my study coach\n"""
        },
    ],
)
thread_id = thread.id
print(thread_id)


# # === Hardcode our ids ===
asistant_id = "asst_2tickfgYPMUENpSIjK7t2fk6"