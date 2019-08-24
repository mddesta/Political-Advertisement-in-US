from flask import Flask, render_template, redirect,current_app
from flask_pymongo import PyMongo
import scrape_ads

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://<dbuser>:<dbpassword>@ds263917.mlab.com:63917/heroku_qkrmp17l"
mongo=PyMongo(app)

@app.route("/")
def home():
    return render_template("Index.html",)

#Adding the other pages
@app.route("/projectInformation")
def projectInformation():
    return render_template("Project Information.html")

@app.route("/aboutus")
def aboutus():
    return render_template("About Us.html")

@app.route("/foreigninfluence")
def foreigninfluence():
    return render_template("Foreign Influence.html")

if __name__ == "__main__": 
    app.run(debug=False)