import urllib.request
import re

url = "https://success4.us"
fp = urllib.request.urlopen(url)
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

data = []
img_link = []

def extract(mystr):
    # return [match[1] for match in HTML_TAG_REGEX.findall(mystr)]

    for match in HTML_TAG_REGEX.findall(mystr):
        data.append(match[1])

    for match in IMG_TAG_REGEX.findall(mystr):
        img_link.append(match[1])

HTML_TAG_REGEX = re.compile(r'<a[^<>]+?href=([\'\"])(.*?)\1', re.IGNORECASE)
# HTML_TAG_REGEX = re.compile(r'<a[^<>]+?href=([\'\"])(.*?)\1', re.IGNORECASE)

# IMG_TAG_REGEX = re.compile(r'<img([^>]*[^/])>')
IMG_TAG_REGEX = re.compile(r'<img[^<>]+?src=([\'\"])(.*?)\1')


extract(mystr)

for i in img_link:
    print(i)

# print(img_link)
