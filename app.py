import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

system_prompt = """
You are an AI assistant that answers ONLY questions strictly related to India.

Allowed topics include:
- Indian history
- Indian geography
- Indian politics
- Indian culture
- Indian economy
- Indian sports
- Indian constitution
- Indian leaders
- Indian current affairs

If a question is even slightly unrelated to India,
you MUST respond with EXACTLY this sentence:

"I am sorry, I can only talk about India."

Rules:
- Do not modify the sentence.
- Do not explain why.
- Do not add extra text.
- Do not apologize differently.
- Do not provide partial answers.
"""

st.title("🇮🇳 India-Only AI Assistant")

user_input = st.text_input("Ask a question about India:")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    answer = response.choices[0].message.content
    st.write(answer)
