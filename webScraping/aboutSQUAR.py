# add directories for calling submodule
import os, sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)


from urllib.request import urlopen
from bs4 import BeautifulSoup


def readAboutSQUAR(): 
    aboutObj = {}
    aboutPageInital = urlopen("https://www.squ.edu.om/squ-ar/%D8%B9%D9%86-%D8%A7%D9%84%D8%AC%D8%A7%D9%85%D8%B9%D8%A9/%D8%A7%D9%84%D8%B1%D8%A4%D9%8A%D8%A9-%D9%88%D8%A7%D9%84%D8%B1%D8%B3%D8%A7%D9%84%D8%A9-%D9%88%D8%A7%D9%84%D8%A3%D9%87%D8%AF%D8%A7%D9%81") 
    aboutPageHtml = aboutPageInital.read().decode('utf-8')
    aboutPageSoup = BeautifulSoup(aboutPageHtml, "html.parser")
    aboutParagragh_html = aboutPageSoup.find_all('div', {'id': 'dnn_ctr949_HtmlModule_lblContent'})[0]
    aboutParagraghHtmlFindText = aboutParagragh_html.find_all("p")
    findUlVaules = aboutParagragh_html.find_all("ul")[0].find_all("li")
    extendValues = list()
    for item in findUlVaules:
      extendValues.append(item.text)
    aboutObj.update({
        "الرؤية": {
            "subText": [str(aboutParagraghHtmlFindText[1].text)],
        }, 
        "الرسالة":  {
            "subText": [str(aboutParagraghHtmlFindText[3].text)],
        },
        "القيم": {
            "subText":  [str(aboutParagraghHtmlFindText[5].text)],
            "extend": extendValues,
        }
    })
    return aboutObj
