# read data from squ.edu.om main page 
# 
# 


from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.squ.edu.om/'
page = urlopen(url + 'About') 
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, "html.parser")

# extract with id content in About page
aboutParagragh_html = soup.find_all('div', {'id': 'dnn_ctr1029_HtmlModule_lblContent'}) 
aboutText = aboutParagragh_html[0].text.strip()
# print(aboutText.split("   ")[0])

#mission, values, vision

pageAbout = urlopen(url+'/About' + '/Mission-Vision-and-Values')
html_aboutPage = pageAbout.read().decode('utf-8')
soup_aboutPage = BeautifulSoup(html_aboutPage, "html.parser") 
#extract info from url
MSV_html = soup_aboutPage.find_all('div', {'id':'dnn_ctr700_ModuleContent'})
MSV_titles = MSV_html[0].find_all('h2')
MSV_subText = MSV_html[0].find_all('p')
MSV_extends = MSV_html[0].find_all('ul') #  only one item belongs to values Update oct/2021

# print(MSV_subText[4].text)

MSV_dataObject = []
for index in range(len(MSV_titles) - 1):
    MSV_dataObject.append({
        'title' : MSV_titles[index].text,
        'subText' : MSV_subText[index].text if index == 0 else MSV_subText[index+1].text,
        'extend' : []
    })
# update Values 
MSV_dataObject[2]['subText'] = MSV_subText[4].text
for extend in MSV_extends[0].find_all('li'):
    MSV_dataObject[2]['extend'].append(extend.text)

print(MSV_dataObject)

print(23)