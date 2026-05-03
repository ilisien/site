from flask import Flask, render_template, request, session, redirect, url_for
from functools import wraps
import os
from envsecrets import SECRET_KEY, PASSWORD

app = Flask(__name__)
app.secret_key = SECRET_KEY

MOBILE_UA_TOKENS = ("mobi", "android", "iphone", "ipod", "windows phone", "blackberry", "opera mini", "iemobile")

@app.after_request
def add_cache_headers(response):
    if request.path.endswith('.css'):
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    return response

def is_mobile():
    ua = (request.headers.get("User-Agent") or "").lower()
    return any(tok in ua for tok in MOBILE_UA_TOKENS)

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("auth"):
            return redirect(url_for("home"))
        return f(*args, **kwargs)
    return decorated

@app.route("/")
def home():
    return render_template("home.html", is_mobile=is_mobile())

@app.route("/login", methods=["POST"])
def login():
    if request.form.get("password").lower() == PASSWORD:
        session["auth"] = True
        return redirect(request.form.get("next", "/"))
    return redirect("/?error=1#gate-writing")


@app.route("/writing")
@requires_auth
def writing():
    return render_template("writing.html", is_mobile=is_mobile())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)