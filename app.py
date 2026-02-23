from flask import Flask, url_for, render_template

app = Flask(__name__)

url_for('static', filename='style.css')

@app.route("/")
def home():
    return render_template()