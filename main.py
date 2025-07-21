import openai
from openai import OpenAI
import os
import dotenv
import json
from outlook.imap import receive_emails_outlook
from outlook.smtp import send_email_outlook
import time
import asyncio

dotenv.load_dotenv()

# bot
email_address = os.getenv("APP_MAIL")
app_password = os.getenv("APP_PASSWORD")
# user
recipient_email = os.getenv("TARGET_MAIL")


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4.1-nano"

with open("prompt.md", "r") as f:
    prompt = f.read()




def answer_maker(content):
    response = client.chat.completions.create(
        model = model,
        messages = [
            {"role" : "system", "content" : f"{prompt}"},
            {"role" : "system", "content" : f"You are a helpful assistant."},
            {"role": "user", "content": f"{content}"}
        ],
        temperature=0,



    )
    return response.choices[0].message.content
#
# def trigger():
#     receive_emails_outlook(
#         email_address =
#     )
#
# def main():
#
# while True :
#     time.sleep(1)
#     msg = trigger()
#     if msg :
#         answer = answer_maker(msg)
#         send_email_outlook(
#             sender_email = email_address,
#             app_password = app_password,
#             recipient_email = recipient_email,
#             subject = "discord api py-cord",
#             body = answer
#         )
#
#
data = answer_maker("test")
send_email_outlook(

    sender_email=email_address,
    app_password=app_password,
    recipient_email=recipient_email,
    subject="discord api py-cord",
    body=data
)






"""
send_email_outlook(
    sender_email="you@outlook.com",
    app_password="your_app_password",
    recipient_email="target@example.com",
    subject="테스트 메일",
    body="이건 테스트용 메일입니다."
)

receive_emails_outlook(
    email_address="you@outlook.com",
    app_password="your_app_password",
    limit=3
)
"""