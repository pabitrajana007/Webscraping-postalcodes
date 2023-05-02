#  Script to scrape Australian postal codes from geonames.org
#
#                           by Pabitra Jana
########################################################################

#Packages
import requests
from tabulate import tabulate
from bs4 import BeautifulSoup

import json


# Make HTTP GET request
response = requests.get('https://www.geonames.org/postalcode-search.html?q=&country=AU')
#print(response.status_code)

#parse our content
content = BeautifulSoup(response.text, 'lxml')


# create an empty dictionary to store the table data
table_dict = {}

print(type(table_dict))

#table = content.find("table", {"class": "restable"})
rows = content.find_all("tr")

# iterate over each row and extract the data from the columns using the 'td' tag
for row in rows:
    cols = row.find_all('td')
    if cols:
        cols = [col.text.strip() for col in cols]
        # use the first column as the key for the row dictionary
        key = cols[0]
        # use the remaining columns as values in the row dictionary
        values = cols[1:]
        table_dict[key] = dict(zip(['Place', 'Code', 'Country', 'State', 'City'], values))

# print the resulting dictionary
#print(table_dict)

con_lis = list(table_dict.items())

# Remove the first element of the list
con_lis.pop(0)

# Remove empty dictionaries from the list
new_list = [item for item in con_lis if bool(item[1])]

#print("Converted dict to list:",new_list)

# Convert the list of dictionaries to a formatted JSON string
json_string = json.dumps(new_list, indent=4)

# Print the formatted JSON string
print(json_string)





# string_unicode = con_lis
# string_encode = string_unicode.encode("ascii", "ignore")
# string_decode = string_encode.decode()
# print(string_decode)