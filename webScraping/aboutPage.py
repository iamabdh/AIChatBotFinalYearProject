# add directories for calling submodule
import os, sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)



# Read SQU main page and resolve the request in object format
# The object requested as model from tensorflow equation 



from urllib.request import urlopen
from bs4 import BeautifulSoup

# Requested url that will get html pages 
url = 'https://www.squ.edu.om/'

def readAboutSQU():
    aboutObj = {}
    aboutPageInital = urlopen(url + 'About') 
    aboutPageHtml = aboutPageInital.read().decode('utf-8')
    aboutPageSoup = BeautifulSoup(aboutPageHtml, "html.parser")  

    # extract with id content in About page
    aboutParagragh_html = aboutPageSoup.find_all('div', {'id': 'dnn_ctr1029_HtmlModule_lblContent'}) 
    aboutText = aboutParagragh_html[0].text.strip().split("   ")[0]


    # store every infos in aboutObj
    aboutObj.update({
        "aboutText" : {
            "subText" : [str(aboutText)],
        }
    })

    #mission, values, vision

    pageAbout = urlopen(url+'/About' + '/Mission-Vision-and-Values')
    html_aboutPage = pageAbout.read().decode('utf-8')
    soup_aboutPage = BeautifulSoup(html_aboutPage, "html.parser") 
    #extract info from url
    MSV_html = soup_aboutPage.find_all('div', {'id':'dnn_ctr700_ModuleContent'})
    MSV_titles = MSV_html[0].find_all('h2')
    MSV_subText = MSV_html[0].find_all('p')
    MSV_extends = MSV_html[0].find_all('ul') #  only one item belongs to values Update oct/2021

    for i in range(len(MSV_titles) -1):
        aboutObj.update({
            str(MSV_titles[i].text) : {
                "subText" : [MSV_subText[i].text if i == 0 else MSV_subText[i+1].text],
                "extend" : [] 
            }
        })


    aboutObj.get('Values').get('subText').append(MSV_subText[4].text)


    for extend in MSV_extends[0].find_all('li'):
        aboutObj.get('Values').get('extend').append(extend.text)

    return aboutObj


print(readAboutSQU("Muhammad Shafiq"))