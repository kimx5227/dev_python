import requests
from bs4 import BeautifulSoup

r = requests.get("https://safe-campus.umn.edu/return-campus/university-planning-response")
soup = BeautifulSoup(r.text, "html.parser")
steps = soup.find("div", {"data-block-plugin-id" : "inline_block:step_graphic"})
step_labels = steps.find_all("div", {"class" : "field__label"})
step_details = steps.find_all("p")
x = {}
for i in range(0, len(step_details)):
    x[step_labels[i].text] = step_details[i].text
print("{:<10} {:<10} ".format('Step #', "Details"))
for key, value in x.items():
    print ("{:<10} {:<10} ".format(key, value))
