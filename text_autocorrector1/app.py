from flask import Flask, render_template, request
from src.autocorrect import AutoCorrector

def load_words(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().split()

app = Flask(__name__)

word_list = load_words("data/big.txt")
autocorrector = AutoCorrector(word_list)

@app.route("/", methods=["GET", "POST"])
def index():
    corrected = ""
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        corrected = autocorrector.correct_sentence(text)

    return render_template("index.html", text=text, corrected=corrected)

if __name__ == "__main__":
    app.run(debug=True)