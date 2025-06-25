import requests
from bs4 import BeautifulSoup
import csv

url = 'https://github.com/trending'
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

repos = soup.find_all("h2", class_="h3 lh-condensed")
results = []

for i in range(5):
    a_tag = repos[i].find('a')
    repo_name = a_tag.text.strip()
    repo_link = "https://github.com" + a_tag.get('href')
    results.append([repo_name, repo_link])
    print(f"Repository Name: {repo_name}")
    print(f"Link: {repo_link}")

with open("trending_repos.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Repository Name", "Link"])
    writer.writerows(results)

print("Saved top 5 trending repositories to trending_repos.csv")
