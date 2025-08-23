from bs4 import BeautifulSoup


def get_data(response):
    soup = BeautifulSoup(response, 'html.parser')
    h1 = soup.find('h1')
    h1_text = h1.get_text() if h1 else ""
    title = soup.title.string.strip() if soup.title else ""
    description = soup.find("meta", attrs={"name": "description"})
    description_text = description["content"] if description else ""

    return {
        "h1": h1_text,
        "title": title,
        "description": description_text
    }

