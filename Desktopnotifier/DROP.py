import requests
from bs4 import BeautifulSoup


def saleGames():
    URL = "https://www.epicgames.com/store/en-US/browse?sortBy=releaseDate&sortDir=DESC&priceTier=tierDiscouted&count=40&start=0"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find(class_="css-cnqlhg")

    game_elements = result.find_all("li", class_="css-lrwy1y")
    num = len(game_elements)

    Sg = []

    for game_element in game_elements:
        game_info = game_element.find("a", class_="css-1jx3eyg")
        Sg.append(game_info.text.strip())
        game_info.text.strip()


    print(Sg)
    print(num)