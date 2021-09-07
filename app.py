from enum import unique
from flask import Flask, render_template, request, redirect, session
from brain import shorten, get_original

app = Flask(__name__)

with open("details.txt", 'r') as file:
    application_name = file.read()
    
@app.route('/url', methods =["GET", "POST"])
def url():
    if request.method == "POST":
       url_to_shorten = request.form.get("url_original")
       short_list = shorten(url_to_shorten)
       return render_template('search.html', short_list=short_list, application_name=application_name)

@app.route('/go_temp', methods =["GET", "POST"])
def go_temp():
    if request.method == "POST":
        short_thingy = str(request.form.get("play_btn"))
        return redirect(f'/go/{short_thingy}')

@app.route('/go/<short_thingy>')
def go(short_thingy):
    original_thingy = get_original(short_thingy)
    return redirect(original_thingy, code=302)

@app.route('/license')
def license_page():
    return render_template('license.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/')
def home():
    return render_template('home.html')