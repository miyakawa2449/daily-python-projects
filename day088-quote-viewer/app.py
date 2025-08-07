from flask import Flask, render_template
import json
import random

app = Flask(__name__)

def load_quotes():
    with open("quotes.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def index():
    quotes = load_quotes()
    selected_quote = random.choice(quotes)
    return render_template("index.html", quote=selected_quote)

if __name__ == "__main__":
    app.run(debug=True)
