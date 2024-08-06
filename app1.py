import streamlit as st
from googletrans import Translator
from transformers import pipeline

# Initialize the translator and summarizer
translator = Translator()
summarizer = pipeline("summarization", model="lidiya/bart-large-xsum-samsum")

def translate_and_summarize(text):
    try:
        # Translate the Arabic text to English
        translated_text = translator.translate(text, src='ar', dest='en').text

        # Summarize the translated text
        summary_result = summarizer(translated_text, max_length=150, min_length=30, length_penalty=2.0)
        summary = summary_result[0]['summary_text']
        
        return translated_text, summary
    except Exception as e:
        return f"An error occurred: {e}", ""

st.title("Arabic Text Translator and Summarizer")

# Input box for Arabic text
arabic_text = st.text_area("Enter Arabic text here:")

if st.button("Translate and Summarize"):
    if arabic_text:
        translation, summary = translate_and_summarize(arabic_text)
        st.subheader("Translation:")
        st.write(translation)
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some Arabic text.")
