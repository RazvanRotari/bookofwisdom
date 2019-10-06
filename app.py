from flask import Flask, escape, request, render_template, redirect
import json
import os

app = Flask(__name__)

DATA_FILE= os.getenv("BW_DATA_FILE", "/data/book.json");

def read_score():
    with open(DATA_FILE, "r") as data:
        scores = json.load(data)
        print(scores)
        return scores


def write_score(score):
    with open(DATA_FILE, "w") as data:
        return json.dump(score, data)


def save_battle(score):
    write_score(score)
    return redirect("/")


def store(name, quote):
    quotes = read_score()
    user_quotes = quotes.get(name, [""])
    user_quotes.append(quote)
    quotes[name] = user_quotes
    return quotes

def create_batle_page():
    scores = read_score()
    return render_template("battle.html", scores=scores)


@app.route('/', methods=['GET', 'POST'])
def battle():
    if request.method == "GET":
        return create_batle_page()
    else:
        print(request.form)
        scores = store(request.form["name"], request.form["quote"])
        return save_battle(scores)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
