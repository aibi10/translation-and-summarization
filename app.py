from flask import Flask, render_template, request
from googletrans import Translator
from transformers import pipeline

app = Flask(__name__)

# Initialize the translator and summarizer
translator = Translator()
summarizer = pipeline("summarization", model="lidiya/bart-large-xsum-samsum")

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ""
    summary = ""
    if request.method == 'POST':
        arabic_text = request.form['arabic_text']
        try:
            # Translate the Arabic text to English
            translated_text = translator.translate(arabic_text, src='ar', dest='en').text

            # Summarize the translated text
            summary_result = summarizer(translated_text, max_length=150, min_length=30, length_penalty=2.0)
            summary = summary_result[0]['summary_text']
            
            translation = translated_text
        except Exception as e:
            translation = f"An error occurred: {e}"
    
    return render_template('index.html', translation=translation, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
