import os

import psycopg2
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    url_for,
    request,
    redirect
)

from page_analyzer.database import Urls


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
conn = psycopg2.connect(DATABASE_URL)
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route("/")
def index():
    return render_template(
        "index.html",
    )

@app.route("/urls", methods=["POST"])
def urls_post():
    urls = Urls()
    url = request.args.get('url')
    urls.save(url)
    return redirect(url_for("index"))


