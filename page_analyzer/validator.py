from urllib.parse import urlparse

import validators


def validate(url):
    errors = {}

    if not validators.url(url):
        errors["url"] = "Некорректный URL"
    
    elif url == "":
        errors["url"] = "URL не может быть пустым"

    elif len(url) > 255:
        errors["url"] = ("Слишком длинный URL. "
        "URL должен быть короче 256 символов")

    return errors


def normalize(url):
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}"