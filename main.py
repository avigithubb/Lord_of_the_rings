from flask import Flask, render_template, redirect, url_for, request
import requests
from pprint import pprint
import os


app = Flask(__name__)

# API_password = LungShao
# Artsy_API_Pass = Meruem321@
EMAIL = "avishek.npt@gmail.com"
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
API = "https://the-one-api.dev/v2"
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}



@app.route("/", methods=["GET", "POST"])
def home():
    # response = requests.get(API, headers=headers)
    # pprint(response.json())
    return render_template("index.html")


@app.route("/all_movies", methods=["GET", "POST"])
def all_movies():
    response = requests.get(API+"/movie", headers=headers)
    # print(response.json())
    return render_template("movies.html", movies = response.json()["docs"])


@app.route("/movies/<movie_id>", methods=["GET", "POST"])
def i_movie(movie_id):
    # movie_id = request.args.get("movie_id")
    response = requests.get(API+"/movie/"+movie_id, headers=headers)
    # print(response.json())
    return render_template("movies.html", my_movie= response.json()["docs"])



@app.route("/quotes/<movie_id>", methods=["GET", "POST"])
def quotes(movie_id):
    return render_template("quotes.html")


@app.route("/all_characters", methods=["GET", "POST"])
def all_characters():
    if request.method == "POST":
        name = request.form.get("character_name").title()
        response = requests.get(API+f"/character?name={name}", headers=headers)
        if response.json()["docs"] == []:
            response = requests.get(API+f"/character?race={name}", headers=headers)
            if response.json()["docs"] == []:
                return render_template("all_characters.html", message="No Character or Race exists Please Try Again!")

        return render_template("all_characters.html", characters=response.json()["docs"])
    response = requests.get(API+"/character", headers=headers)
    return render_template("all_characters.html", characters = response.json()["docs"])

@app.route("/info/<id>", methods=["GET", "POST"])
def character_info(id):
    response = requests.get(API+"/character/"+id, headers=headers)
    return render_template("characters.html", info=response.json()["docs"], character_name = response.json()["docs"][0]["name"])

@app.route("/quote/<id>", methods=["GET", "POST"])
def character_quote(id):
    my_id = f"{id}"
    response_character = requests.get(API+"/character/"+id, headers=headers)
    response_quote = requests.get(API+f"/character/{my_id}/quote", headers=headers)
    # pprint(response_quote.json())
    return render_template("characters.html", quotes=response_quote.json(), character_name = response_character.json()["docs"][0]["name"])


@app.route("/movie_info/<movie_id>", methods=["GET"])
def movie_info(movie_id):
    print("success")
    response = requests.get(API+"/movie/"+movie_id, headers=headers)
    return response.json()

@app.route("/book_info/<book_id>", methods=["GET"])
def book_info(book_id):
    response = requests.get(API+f"/book/{book_id}/chapter", headers=headers)
    # print(response.json())
    return response.json()

@app.route("/movie_quote/<movie_id>", methods=["GET", "POST"])
def movie_quote(movie_id):
    global dialogs, movie_name
    print(movie_id)
    response_movie = requests.get(API+"/movie"+movie_id, headers=headers)
    response = requests.get(API+f"/movie/{movie_id}/quote", headers=headers)
    movie_name= response_movie.json()["docs"]["name"]
    dialogs = response.json()["docs"]
    # print(response.json())
    return render_template("quotes.html", dialogs=response.json()["docs"])

@app.route("/movie_dialog", methods=["GET", "POST"])
def dialog():
    global dialogs, movie_name
    return render_template("quotes.html", dialog = dialogs, movie=movie_name)

@app.route("/all_books", methods=["GET", "POST"])
def all_books():
    response = requests.get(API+"/book", headers=headers)
    return render_template("movies.html", books = response.json()["docs"])

if __name__ == "__main__":
    app.run(debug=True)