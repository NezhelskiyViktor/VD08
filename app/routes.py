from flask import Flask, render_template
from app import app
import requests
from googletrans import Translator


@app.route('/', methods=['GET', 'POST'])
def index():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    data = response.json()

    original_text = data['content']
    author = data['author']

    # Переводим текст цитаты на русский
    translator = Translator()
    translated_text = translator.translate(original_text, dest='ru').text

    # Переводим автора на русский
    translated_author = translator.translate(author, dest='ru').text

    return render_template('index.html', original_text=original_text, author=author, translated_text=translated_text,
                           translated_author=translated_author)
