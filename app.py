#  Script to scrape Australian postal codes from geonames.org
#
#                           by Pabitra Jana
########################################################################

#Packages
import requests

from bs4 import BeautifulSoup
#import pandas as pd

# Make HTTP GET request
response = requests.get('https://www.geonames.org/postalcode-search.html?q=&country=AU')
print(response.status_code)

#parse our content
content = BeautifulSoup(response.text, 'lxml')

print(content)













# Extract table data
#table = content.find('table', {'class': 'restable'})

# Create a list to store data
#data = []

# Extract table rows
# for row in table.findAll('tr'):
#     cols = row.findAll('td')
#     # Extract place and code from table columns
#     place = cols[1].text.strip()
#     code = cols[2].text.strip()
#     # Add place and code to data list
#     data.append([place, code])

# # Create a pandas dataframe and print it as a table
# df = pd.DataFrame(data, columns=['Place', 'Code'])
# print(df.to_string(index=False))



