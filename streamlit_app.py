import streamlit as st
from openai import OpenAI

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

client = OpenAI(
  base_url="http://192.168.29.194:1234",
  api_key="",
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "Project", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="google/gemma-3n-e4b",
  messages=[
              {
                "role": "user",
                "content": st.text_input("Enter your message:")
              }
            ]
)
st.write(completion.choices[0].message.content)
