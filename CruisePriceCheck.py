# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

# Import re for string stripping
import re

# Import datetime for date and times
from datetime import datetime

# open price file for reading
priceFile = open('price.txt', 'r')
firstLine = priceFile.readline()
for lastLine in priceFile:
    pass
priceFile.close()

# open price file for appending
priceFile = open('price.txt', 'a')

# set URL
url = "https://www.royalcaribbean.com/cruises/itinerary/7-night-greece-italy-with-late-stays-in-santorini-mykonos-from-rome-civitavecchia-on-odyssey/OY07ROM-2173932233?sail-date=2021-08-22&currency=USD&country=USA&dates_maxDate=06%2F30%2F2021&dates_minDate=06%2F01%2F2021"

# set the headers like we are a browser,
Headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}

# download the homepage
print('Downloading homepage...')
response = requests.get(url, headers=Headers)

# parse the downloaded homepage and grab all text, then
print('Creating soup...')
soup = BeautifulSoup(response.text, "lxml")

# find all span tags
print('Finding price...')
spanTags = soup.find_all('span')

# loop through span spanTags
for tag in spanTags:
    # check if tag contains lowPrice
    if(str(tag).count('lowPrice') > 0):
        # strip string of all nonnumeric values
        priceTag = tag
        print('Before stripping: ', priceTag)
        priceTag = re.sub("[^0-9 , .]", "", str(priceTag))
        print('After stripping: ', priceTag)

        # substring to remove decimal point
        placeOfPt = str(priceTag).find('.')
        if(placeOfPt != -1):
            priceTag = priceTag[0 : int(placeOfPt)]
        print('Integer Price: ', priceTag)
        priceTag = re.sub(" ", "", str(priceTag))


# append to price firstLine
priceFile.write(str(datetime.now()) + "\n")
priceFile.write("Price of ticket: " + "\n" + str(priceTag) + "\n")
priceFile.close()

# email
