from flask import Flask, render_template, flash, request, redirect, url_for
import requests 
import smtplib
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SECRET_KEY'

@app.route("/")
@app.route("/home")
def home():
	return render_template("front.html")

@app.route("/Menu")
def menu():
	return render_template("menu.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():

	name = request.form.get("name")
	date = request.form.get("date")
	email = request.form.get("email")
	time = request.form.get("time")
	phone = request.form.get("phone")
	people = request.form.get("people")
	nachricht = request.form.get("nachricht")

	if name or people != None:
		message = "Danke fuer Ihre Reservierung bei Restaurant Online"
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls()
		server.login("yourGmailusername", "yourpassword")
		server.sendmail("yourGmailusername", email, message)

	return render_template("contact.html")


@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/Bestellen")
def order():
	return render_template("order.html")

@app.route("/abc")
def reservierung():
	return render_template("abc.html")

@app.route("/covid")
def covid():
	return render_template("covid.html")



if __name__ == "__main__":
	app.run(port=5000, debug=True)