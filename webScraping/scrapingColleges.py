from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.squ.edu.om/'
page = urlopen(url + 'agriculture/About-College') 
html = page.read().decode('utf-8')
aboutCAMS_html = BeautifulSoup(html, "html.parser")

aboutParagragh_html = aboutCAMS_html.find_all('div', {'class': 'resp_margin'}) 


print(aboutParagragh_html[0].find_all('p'))