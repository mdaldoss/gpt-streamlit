import openai
import streamlit as st

def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    try: 
        resp = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=.5,
            max_tokens=1000,
        )["choices"][0]["text"]
        st.session_state["summary"] = resp
    except:
        st.write('There was an error =(')