import urllib.request
import json

f = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1430672.json')

jsonData = json.loads(f.read())

list_comments = jsonData["comments"]

sum = 0
for c in list_comments:
  count = int(c["count"])
  sum += count

print("total comments =", sum)