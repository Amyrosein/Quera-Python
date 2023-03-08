from bs4 import BeautifulSoup


def process(path):
    with open(path) as f:
        soup = BeautifulSoup(f, "html.parser")
        return len(soup.find_all('a'))
