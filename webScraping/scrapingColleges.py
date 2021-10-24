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

#Department of Animal and Veterinary Sciences
page1 = urlopen(url + 'agriculture/Academic-Department/Animal-and-Veterinary-Sciences/Description') 
html1 = page1.read().decode('utf-8')
aboutAVS_descr_html = BeautifulSoup(html1, "html.parser")

AVS_descrParagragh_html = aboutAVS_descr_html.find_all('div', {'id': 'tab_item-1723-0'})[0].find_all('p') 

AVSdescr_text = str()

for textItem in AVS_descrParagragh_html:
    AVSdescr_text += textItem.text +'\n'

print(AVSdescr_text)

#Department of Plant Sciences
page2 = urlopen(url + 'agriculture/Academic-Department/Plant-Sciences/Description') 
html2 = page2.read().decode('utf-8')
aboutPS_descr_html = BeautifulSoup(html2, "html.parser")

PS_descrParagragh_html = aboutPS_descr_html.find_all('div', {'id': 'tabposition_1724'})[0].find_all(['p','li','span']) 

PSdescr_text = str()

for textItem in PS_descrParagragh_html:
    PSdescr_text += textItem.text +'\n'

print(PSdescr_text)

#epartment of Food Science and Nutrition
page3 = urlopen(url + 'agriculture/Academic-Department/Food-Science-and-Nutrition/Description') 
html3 = page3.read().decode('utf-8')
aboutFSN_descr_html = BeautifulSoup(html3, "html.parser")

FSN_descrParagragh_html = aboutFSN_descr_html.find_all('div', {'id': 'tabposition_1725'})[0].find_all(['p','li','span']) 

FSNdescr_text = str()

for textItem in FSN_descrParagragh_html:
    FSNdescr_text += textItem.text +'\n'

print(FSNdescr_text)

#Department of Marine Science and Fisheries
page4 = urlopen(url + 'agriculture/Academic-Department/Marine-Science-and-Fisheries/Description') 
html4 = page4.read().decode('utf-8')
aboutMSF_descr_html = BeautifulSoup(html4, "html.parser")

MSF_descrParagragh_html = aboutMSF_descr_html.find_all('div', {'id': 'tabposition_1731'})[0].find_all(['p','li','span']) 

MSFdescr_text = str()

for textItem in MSF_descrParagragh_html:
    MSFdescr_text += textItem.text +'\n'

print(MSFdescr_text)

#Department of Natural Resource Economics
page5 = urlopen(url + 'agriculture/Academic-Department/Natural-Resource-Economics/Description') 
html5 = page5.read().decode('utf-8')
aboutNRE_descr_html = BeautifulSoup(html5, "html.parser")

NRE_descrParagragh_html = aboutNRE_descr_html.find_all('div', {'id': 'tabposition_1733'})[0].find_all(['p','li','span']) 

NREdescr_text = str()

for textItem in NRE_descrParagragh_html:
    NREdescr_text += textItem.text +'\n'

print(NREdescr_text)

#Department of Soils, Water and Agricultural Engineering
page6 = urlopen(url + 'agriculture/Academic-Department/Soils-Water-and-Agricultural-Engineering/Description') 
html6 = page6.read().decode('utf-8')
aboutSWAE_descr_html = BeautifulSoup(html6, "html.parser")

SWAE_descrParagragh_html = aboutSWAE_descr_html.find_all('div', {'id': 'tabposition_1732'})[0].find_all(['p','li','span']) 

SWAEdescr_text = str()

for textItem in SWAE_descrParagragh_html:
    SWAEdescr_text += textItem.text +'\n'

print(SWAEdescr_text)