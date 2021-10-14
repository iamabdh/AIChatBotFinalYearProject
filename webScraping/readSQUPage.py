# read data from squ.edu.om main page 
# 
# 
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.squ.edu.om/'
page = urlopen(url + 'About') 
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())
