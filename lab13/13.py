import urllib.request
from bs4 import BeautifulSoup

# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_1430669.html')

# read the data from the URL and print it
data = webUrl.read()
soup = BeautifulSoup(data, 'html.parser')

spans = soup.find_all('span')
lines = [int(span.get_text()) for span in spans]
print("total lines: ", len(lines))
print("======================")

print("Total comments: ", sum(lines))