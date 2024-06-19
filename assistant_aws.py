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

# # ==  Create our Assistant (Uncomment this to create your assistant) ==
# personal_trainer_assis = client.beta.assistants.create(
#     name="AWS Tutor",
#     instructions="""You are an AWS expert tutor, AWS assistant, and AWS educator.\n
#     Provide detailed answers to AWS certification questions, explain AWS concepts with practical examples, generate AWS practice exams, and assist answering AWS quizzes and AWS practice exams.\n
#     Diagnose students' gaps in AWS knowledge, identify topics students need to study and provide additional explanations, examples and AWS practice exam questions to address the AWS knowledge gaps""",
#     tools=[{"type": "code_interpreter"}, {"type": "file_search"}],
#     model=model,
#     # response_format={ "type": "json_object"},
#     response_format="auto",
# )
# asistant_id = personal_trainer_assis.id
# print(asistant_id)



# question_object = {
#     "difficulty": "easy",
#     "layout": "optionsOnly",
#     "question_text": "Which cloud deployment model best describes AWS?",
#     "score": 1,
#     "answer": {
#         "answer_image": "",
#         "answer_text": "<p>AWS is primarily a public cloud deployment model where a user can provision resources in the public cloud. Resources are provisioned for open use by the general public, business, academic, government organizations, or some combination of them. Resources exist on the premises of the cloud provider.</p>",
#         "values": [
#             {
#                 "type": "option_id",
#                 "index": 0,
#                 "value": "2d59aae0-0148-4ef3-8181-33b31bb5c8f8"
#             }
#         ]
#     },
#     "label": "Cloud Concepts",
#     "type": "multiple_answer_1",
#     "question_id": "4275112b-dbab-4f6f-ac29-4dc48f250d4c",
#     "answer_image": "null",
#     "question_image": "null",
#     "options": [
#         {
#             "option_id": "2d59aae0-0148-4ef3-8181-33b31bb5c8f8",
#             "option_header": "Public Cloud",
#             "option_text": "",
#             "option_image": "null"
#         },
#         {
#             "option_id": "958a9f13-2d6b-4334-ad6c-685fbf35a251",
#             "option_header": "Private Cloud",
#             "option_text": "",
#             "option_image": "null"
#         },
#         {
#             "option_id": "062a754e-3c24-45c8-bd0c-d44a9f2f0c76",
#             "option_header": "Hybrid Cloud",
#             "option_text": "",
#             "option_image": "null"
#         },
#         {
#             "option_id": "cf3cd67f-6880-4e76-b375-ca8adedfe349",
#             "option_header": "Community Cloud",
#             "option_text": "",
#             "option_image": "null"
#         }
#     ]
# }

# # Calculate the expiry time 15 minutes from now
# expiry_time = datetime.now() + timedelta(minutes=15)

# # # === Thread (uncomment this to create your Thread) ===
# thread = client.beta.threads.create(
#     messages=[
#         {
#             "role": "assistant", "content": "You are in JSON mode."
#         },
#         {
#             "role": "user",
#             "content": f'I\'m answering AWS practice exam and I would like further assistance with the question. Question context: {question_object}',
#         },
#         {
#             "role": "assistant",
#             "content": """Hey there! Quizby is now using the power of AI to help you study more effectively. Let's get started?\n
#             What would you like to do next? Here are some options:\n
#             1. Explain the question, each of the options, and answer the question (Explain question)\n
#             2. Explain the concepts involved and provide examples (Explain Concept)\n
#             3. Generate a practice exam question (Quiz Me)\n
#             4. Be my study coach\n"""
#         },
#     ],
#    expires_at=expiry_time,
# )
# thread_id = thread.id
# print(thread_id)


# # === Hardcode our ids ===
asistant_id = "asst_2tickfgYPMUENpSIjK7t2fk6"
thread_id = "thread_2xwdhfuBZZZCRR1kCU4U9NpU"


message1 = 'Explain the question, each of the options, and answer the question (Explain question)'
message2 = 'Explain the concepts involved and provide examples (Explain Concept)'
message3 = 'Generate a practice exam question on the topic of the question (Quiz Me)'
message4 = 'Be my study coach. Ask me for a prompt on what topic you want to study or revise (Study Coach)'

# ==== Create a Message ====
message = client.beta.threads.messages.create(
    thread_id=thread_id, role="user", content=message4
)

# === Run our Assistant ===


# run = client.beta.threads.runs.create(
#     thread_id=thread_id,
#     assistant_id=asistant_id,
#     max_prompt_tokens=1500,
#     max_completion_tokens=500,
#     expires_at=expiry_time,
#     # instructions="Please address the user as James Bond",
# )





# def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
#     """

#     Waits for a run to complete and prints the elapsed time.:param client: The OpenAI client object.
#     :param thread_id: The ID of the thread.
#     :param run_id: The ID of the run.
#     :param sleep_interval: Time in seconds to wait between checks.
#     """
#     while True:
#         try:
#             run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
#             if run.completed_at:
#                 elapsed_time = run.completed_at - run.created_at
#                 formatted_elapsed_time = time.strftime(
#                     "%H:%M:%S", time.gmtime(elapsed_time)
#                 )
#                 print(f"Run completed in {formatted_elapsed_time}")
#                 logging.info(f"Run completed in {formatted_elapsed_time}")
#                 # Get messages here once Run is completed!
#                 messages = client.beta.threads.messages.list(thread_id=thread_id)
#                 last_message = messages.data[0]
#                 response = last_message.content[0].text.value
#                 print(f"Assistant Response: {response}")
#                 break
#         except Exception as e:
#             logging.error(f"An error occurred while retrieving the run: {e}")
#             break
#         logging.info("Waiting for run to complete...")
# time.sleep(sleep_interval)


# === Run ===
# wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)


# === Run ALTERNATIVE ===
run = client.beta.threads.runs.create(
    thread_id=thread_id,
    assistant_id=asistant_id,
    max_prompt_tokens=1500,
    max_completion_tokens=500,
    # expires_at=expiry_time,
)



while True:
    try:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id, run_id=run.id
        )
        # if run.status == "completed":
        if run.completed_at:
            messages = client.beta.threads.messages.list(
                thread_id=thread_id
            )
            last_message = messages.data[0]
            response = last_message.content[0].text.value
            print(f"Assistant Response: {response}")
            break
        else:
            print(run.status)
    except Exception as e:
        print(f"Error retrieving run: {e}")
    time.sleep(5)


# if run.status == 'completed': 
#   messages = client.beta.threads.messages.list(
#     thread_id=thread_id
#   )
#   print(messages)
# else:
#   print(run.status)


# ==== Steps --- Logs ==
run_steps = client.beta.threads.runs.steps.list(thread_id=thread_id, run_id=run.id)
print(f"Steps---> {run_steps.data[0]}")