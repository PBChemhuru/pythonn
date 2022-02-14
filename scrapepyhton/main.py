import requests
from bs4 import BeautifulSoup

# URL = "https://realpython.github.io/fake-jobs/"
# page = requests.get(URL)
#
# soup = BeautifulSoup(page.content, "html.parser")
# results = soup.find(id="ResultsContainer")
# job_elements = results.find_all("div", class_="card-content")
#
# # for job_element in job_elements:
# #     title_element = job_element.find("h2", class_="title")
# #     company_element = job_element.find("h3", class_="company")
# #     location_element = job_element.find("p", class_="location")
# #     print(title_element.text.strip())
# #     print(company_element.text.strip())
# #     print(location_element.text.strip())
# #     print()
#
# python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
#
# python_job_elements =[
#     h2_element.parent.parent.parent for h2_element in python_jobs
# ]
# for job_element in python_job_elements:
#     title_element = job_element.find("h2", class_="title")
#     company_element = job_element.find("h3", class_="company")
#     location_element = job_element.find("p", class_="location")
#     print(title_element.text.strip())
#     print(company_element.text.strip())
#     print(location_element.text.strip())
# print(python_jobs)


URL = "https://www.epicgames.com/store/en-US/browse?sortBy=releaseDate&sortDir=DESC&priceTier=tierDiscouted&count=40&start=0"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
result = soup.find(class_= "css-cnqlhg")

game_elements = result.find_all("li", class_="css-lrwy1y")

for game_element in game_elements:
    game_info = game_element.find("a", class_="css-1jx3eyg")
    print(game_info.text.strip())