import streamlit as st
import openai
import os

# Set API key
openai.api_key = os.environ["OPENAI_API_KEY"]

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
"""

st.title("🇮🇳 India-Only AI Assistant")

user_input = st.text_input("Ask a question about India:")

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    answer = response["choices"][0]["message"]["content"]
    st.write(answer)
