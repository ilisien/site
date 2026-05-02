from flask import Flask, render_template, request, session, redirect, url_for
from functools import wraps
import os
from envsecrets import SECRET_KEY, PASSWORD

app = Flask(__name__)
app.secret_key = SECRET_KEY

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("auth"):
            return redirect(url_for("home"))
        return f(*args, **kwargs)
    return decorated

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["POST"])
def login():
    if request.form.get("password").lower() == PASSWORD:
        session["auth"] = True
        return redirect(request.form.get("next", "/"))
    return redirect("/?error=1#gate-writing")


@app.route("/writing")
@requires_auth
def writing():
    return render_template("writing.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)