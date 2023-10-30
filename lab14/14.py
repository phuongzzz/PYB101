import urllib.request
import xml.etree.ElementTree as ET

f = urllib.request.urlopen('https://py4e-data.dr-chuck.net/comments_1430671.xml')

tree = ET.parse(f)
root = tree.getroot()

sum = 0
for comment in root.find('comments').findall('comment'):
  count = comment.find('count').text
  sum += int(count)

print("sum =", sum)




# for article in root.findall("PubmedArticle"):
#     article_title = article.find("MedlineCitation").find("Article").find("ArticleTitle")
#     print(article_title.text)