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


page1 = urlopen(url + 'agriculture/Academic-Department/Animal-and-Veterinary-Sciences/Description') 
html1 = page1.read().decode('utf-8')
aboutAVS_descr_html = BeautifulSoup(html1, "html.parser")

AVS_descrParagragh_html = aboutAVS_descr_html.find_all('div', {'id': 'tab_item-1723-0'})[0].find_all('p') 

AVSdescr_text = str()

for textItem in AVS_descrParagragh_html:
    AVSdescr_text += textItem.text +'\n'

print(AVSdescr_text)

page2 = urlopen(url + 'agriculture/Academic-Department/Plant-Sciences/Description') 
html2 = page2.read().decode('utf-8')
aboutPS_descr_html = BeautifulSoup(html2, "html.parser")

PS_descrParagragh_html = aboutPS_descr_html.find_all('div', {'id': 'tab_item-1724-0'})[0].find_all('p') 

PSdescr_text = str()

for textItem in PS_descrParagragh_html:
    PSdescr_text += textItem.text +'\n'

print(PSdescr_text)




