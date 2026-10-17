from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# response = client.chat.completions.create(
#     model="openai/gpt-oss-120b",
#     messages=[
#         {"role": "user", "content": "what are stocls and bonds?"}
#     ],
# )


# response = client.chat.completions.create(
#     model="openai/gpt-oss-120b",
#     messages=[
#         {"role": "system", "content": "Answer it in 2-3 lines in simple languange like a 11th or 12th grader student can understand"},
#         {"role": "user", "content": "what are stocks and bonds?"}
#     ],
# )

# response = client.chat.completions.create(
#     model="openai/gpt-oss-120b",
#     messages=[
#         {"role": "system", "content": "You are a 5-year-old. Answer using only short, simple words"},
#         {"role": "user", "content": "what are stocks and bonds?"}
#     ],
# )

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "You are a invenstment banker"},
        {"role": "user", "content": "what are stocks and bonds?"}
    ],
)




print(response.choices[0].message.content)
