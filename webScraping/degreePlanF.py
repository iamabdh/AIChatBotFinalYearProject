# add directories for calling submodule
import os, sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)




from bs4 import BeautifulSoup
from urllib.request import urlopen
import unicodedata

def degreePlan(year):
    url='https://www.squ.edu.om/engineering/Academic/Undergraduate-Programs/Electrical-and-Computer-Engineering'
    degreelinks=[]
    degreePage = urlopen(url ) 
    html = degreePage.read().decode('utf-8')
    degree_html = BeautifulSoup(html, "html.parser")
    degreePlan_html = degree_html.find_all('div', {'id': 'dnn_ctr6031_View_Index_plLicense'})[0].find_all('a')
    url1='https://www.squ.edu.om'
    degreeLinks=[]
    for link in degreePlan_html:
        degreeLinks.append(link.get('href'))
    # print(degreeLinks[2])
    # exit(1)

    degreeYear=year
    if (degreeYear=='2021') :
        return {'The degree Link: ': str(str(url1)+degreeLinks[0])}
    elif (degreeYear=='2020') :
        return {'The degree Link: ': str(str(url1)+degreeLinks[1])}
    elif (degreeYear=='2019') :
        return {'The degree Link: ': str(str(url1)+degreeLinks[2])}
    elif (degreeYear=='2018') :
        return {'The degree Link: ': str(str(url1)+degreeLinks[3])}
    elif (degreeYear=='2017') :
        return {'The degree Link: ':str( str(url1)+degreeLinks[4])}
    elif (degreeYear=='2016') :
        return {'The degree Link: ': str(str(url1)+degreeLinks[5])}
    elif (degreeYear=='2015') :
        return {'The degree Link: ': str(str(url1)+degreeLinks[6])}
    else:
        return 0


print(degreePlan('2019'))



