from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.squ.edu.om/'
page = urlopen(url + 'agriculture/About-College') 
html = page.read().decode('utf-8')
aboutCAMS_html = BeautifulSoup(html, "html.parser")

CAMSParagragh_html = aboutCAMS_html.find_all('div', {'id': 'tab_item-7237-1'})[0].find_all('p') 

CAMS_text = str()

for textItem in CAMSParagragh_html:
    CAMS_text += textItem.text +'\n'

print(CAMS_text)




