import os

import psycopg2
import requests
from dotenv import load_dotenv
from flask import (
    Flask,
    flash,
    get_flashed_messages,
    redirect,
    render_template,
    request,
    url_for,
)

from page_analyzer.database import Urls
from page_analyzer.parser import get_data
from page_analyzer.validator import normalize, validate

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
    urls = Urls(DATABASE_URL)
    url = request.form.to_dict()
    errors = validate(url["url"])
    if errors:
        flash(errors["url"], "warning")
        return render_template(
            "index.html",
            messages=get_flashed_messages(with_categories=True)
        ), 422
    normalized_url = normalize(url["url"])
    url_info = urls.find_url(normalized_url)
    if url_info is None:
        id = urls.save(normalized_url)
        flash("URL успешно добавлен", "success")
        return redirect(url_for("url_get", id=id))
    flash("URL уже существует", "info")
    urls.conn.close()
    return redirect(url_for("url_get", id=url_info.get("id")))


@app.route("/urls/<int:id>")
def url_get(id):
    urls = Urls(DATABASE_URL)
    url = urls.find_id(id)
    messages = get_flashed_messages(with_categories=True)
    check_info = None
    urls.conn.close()
    return render_template(
        "url.html",
        url=url,
        messages=messages,
        check_info=check_info
        
    )


@app.route("/urls")
def urls_get():
    urls = Urls(DATABASE_URL)
    all_urls = urls.get_all_urls()
    # check = urls.get_check
    messages = get_flashed_messages(with_categories=True)
    urls.conn.close()
    return render_template(
        "urls.html",
        urls=all_urls,
        messages=messages
    )


@app.route("/urls/<int:id>/checks", methods=["POST"])
def checks_post(id):
    urls = Urls(DATABASE_URL)
    url_info = urls.find_id(id)
    try:
        response = requests.get(url_info.get("name"), timeout=1)
        response.raise_for_status()
    except requests.RequestException:
        flash("Произошла ошибка при проверке", "warning")
        return redirect(url_for("url_get", id=id))

    status_code = response.status_code
    print(status_code)
    parsed_data = get_data(response.text)
    parsed_data["url_id"] = id
    parsed_data["status_code"] = status_code
    
    urls.add_url_check(parsed_data)
    flash("Проверка успешно произведена", "success")
    checks = urls.get_url_check(id)
    print(checks)
    urls.conn.close()
    return render_template(
        "url.html",
        checks=checks,
        url=url_info
    )