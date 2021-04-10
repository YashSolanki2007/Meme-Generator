# Making the imports
from flask import Flask, render_template, request
import requests
import random
from flask_frozen import Freezer

app = Flask(__name__)

img = ""
top_text = ""
bottom_text = ""

# Making the login page


@app.route("/", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@app.route("/main", methods=['GET', 'POST'])
def home():
    global img, top_text, bottom_text

    if request.method == "POST":
        webpage = request.form

        top_text = str(webpage['top'])
        bottom_text = str(webpage['bottom'])

        # Taking the url of the api
        url = "https://api.imgflip.com/get_memes"

        # Getting the response from the api
        response = requests.get(url)

        # Taking the response and converting it into a JSON format
        jsonated_response = response.json()

        random_meme_img = random.randint(1, 99)

        img = jsonated_response['data']['memes'][random_meme_img]['url']

    return render_template("index.html", meme_img=img, top_text=top_text, bottom_text=bottom_text)


if __name__ == '__main__':
    app.run(debug=True)
