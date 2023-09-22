import re

url = "https://twitter.com/a5288"
# re.search(r"", url)
test = re.search(r"/(\w+)$", url)
print(test.group(1))