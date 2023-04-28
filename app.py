#  Script to scrape Australian postal codes from geonames.org
#
#                           by Pabitra Jana
########################################################################

#Packages
import requests
from tabulate import tabulate
from bs4 import BeautifulSoup


# Make HTTP GET request
response = requests.get('https://www.geonames.org/postalcode-search.html?q=&country=AU')
#print(response.status_code)

#parse our content
content = BeautifulSoup(response.text, 'lxml')




table = content.find("table", {"class": "restable"})
rows = content.find_all("tr")

data = []

for row in rows:
    cols = row.find_all("td")
    cols = [col.text.strip() for col in cols]
    data.append(cols)

#print(data)

print(type(data))
# print(data[0])
# print(data[1])
# print(data[2])
# print(data[3]) from here data is necessary!! above this is crap!!
# print(data[4])
# print(data[5])
# print(data[6])



for sub_list in data:
    for item in sub_list:
        if item.isdigit():
            print(sub_list)
            break
