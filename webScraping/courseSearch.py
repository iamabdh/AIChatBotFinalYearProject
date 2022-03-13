import os, sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)




from bs4 import BeautifulSoup
from urllib.request import urlopen
import unicodedata

def searchCourse(course):

    url = 'https://www.squ.edu.om/engineering/Academic/Undergraduate-Programs/Electrical-and-Computer-Engineering'

    coursePage = BeautifulSoup(urlopen(url).read().decode('utf-8'), 'lxml').find_all(['p'])
    objectList = []
    for itemTotal in coursePage:
        objectList.append(itemTotal.text.splitlines())


    rquiredObj = []

    for objItem in objectList:
        rquiredObj.append(objItem)

    courseCode = course
    info=str()
    if courseCode is not None:
        for index, courseObj in enumerate(rquiredObj):
            if courseObj[0] != '':
                courseObj=courseObj[0].split()
                for l in courseObj:
                    if courseCode.upper() == l:
                        info=rquiredObj[index]+rquiredObj[index+1]+rquiredObj[index+2]

                        return info
            else:
                courseObj=courseObj[1].split()
                for l in courseObj:
                    if courseCode.upper() == l:
                        info=rquiredObj[index]+rquiredObj[index+1]+rquiredObj[index+2]
                        info=info[1:]

                        return info
    
    

def searchCourseArc(course):
    
    url = 'https://www.squ.edu.om/engineering/Academic/Undergraduate-Programs/Architectural-Engineering'

    coursePage = BeautifulSoup(urlopen(url).read().decode('utf-8'), 'lxml').find_all(['p'])
    objectList = []
    for itemTotal in coursePage:
        objectList.append(itemTotal.text.splitlines())


    rquiredObj = []

    for objItem in objectList:
        rquiredObj.append(objItem)

    courseCode = course
    info=str()
    if courseCode is not None:
        for index, courseObj in enumerate(rquiredObj):
            courseObj=courseObj[0].split()
            
            for l in courseObj:
                if courseCode.upper() == l:
                    info=rquiredObj[index]+rquiredObj[index+1]

                    return info
def searchCourseCIVL(course):
    
    url = 'https://www.squ.edu.om/engineering/Academic/Undergraduate-Programs/-Civil-Engineering'
    course= course[4:]
    coursePage = BeautifulSoup(urlopen(url).read().decode('utf-8'), 'lxml').find_all(['p'])
    objectList = []
    for itemTotal in coursePage:
        objectList.append(itemTotal.text.splitlines())


    rquiredObj = []

    for objItem in objectList:
        rquiredObj.append(objItem)

    courseCode = course
    info=str()
    if courseCode is not None:
        for index, courseObj in enumerate(rquiredObj):
            courseObj=courseObj[0].split()
            
            for l in courseObj:
                if courseCode.upper() == l:
                    info=rquiredObj[index]+rquiredObj[index+1]

                    return info

def searchCourseIndust(course):
    
    url = 'https://www.squ.edu.om/engineering/Academic/Undergraduate-Programs/Industrial-Engineering'
    url2 = 'https://www.squ.edu.om/engineering/Academic/Undergraduate-Programs/Mechanical-Engineering'


    coursePage = BeautifulSoup(urlopen(url).read().decode('utf-8'),'html.parser').find_all('div', {'id': 'ResponsiveTabs_6032'})[0].find_all(['p'])
    coursePage2 = BeautifulSoup(urlopen(url2).read().decode('utf-8'),'html.parser').find_all('div', {'id': 'ResponsiveTabs_6033'})[0].find_all(['p'])
    objectList = []
    for itemTotal in coursePage2:
        objectList.append(itemTotal.text.splitlines())
    for itemTotal in coursePage:
        objectList.append(itemTotal.text.splitlines())
    

    rquiredObj = []

    for objItem in objectList:
        rquiredObj.append(objItem)
    
    courseCode = course
    info=str()
    if courseCode is not None:
        for index, courseObj in enumerate(rquiredObj):
            if courseObj[0] != '':
                courseObj=courseObj[0].split()
                for l in courseObj:
                    if courseCode.upper() == l:
                        info=rquiredObj[index]+rquiredObj[index+1]+rquiredObj[index+2]
                        if len(info[3])<5:
                            info=info[:3]

                        return info
                    
            elif courseObj[0] == '':
                courseObj=courseObj[1].split()
                for l in courseObj:
                    if courseCode.upper() == l:
                        info=rquiredObj[index]+rquiredObj[index+1]+rquiredObj[index+2]
                        info=info[1:]

                        return info

def searchCourseMechat(course):

    url = 'https://www.squ.edu.om/engineering/Academic/Undergraduate-Programs/Mechatronics-Engineering'

    coursePage = BeautifulSoup(urlopen(url).read().decode('utf-8'), 'html.parser').find_all('div', {'id': 'ResponsiveTabs_6034'})[0].find_all(['p'])
    objectList = []
    for itemTotal in coursePage:
        objectList.append(itemTotal.text.splitlines())


    rquiredObj = []

    for objItem in objectList:
        rquiredObj.append(objItem)

    courseCode = course
    info=str()
    if courseCode is not None:
        for index, courseObj in enumerate(rquiredObj):
            if courseObj[0] != '':
                courseObj=courseObj[0].split()
                for l in courseObj:
                    if courseCode.upper() == l:
                        info=rquiredObj[index]+rquiredObj[index+1]+rquiredObj[index+2]+rquiredObj[index+3]
                        if len(info[3])<5:
                            info=info[:3]

                        return info
            else:
                courseObj=courseObj[1].split()
                for l in courseObj:
                    if courseCode.upper() == l:
                        info=rquiredObj[index]+rquiredObj[index+1]+rquiredObj[index+2]+rquiredObj[index+3]
                        info=info[1:]

                        return info

def searchCourseChem(course):

    url = 'https://www.squ.edu.om/engineering/Academic/Undergraduate-Programs/Chemical-and-Process-Engineering'

    coursePage = BeautifulSoup(urlopen(url).read().decode('utf-8'), 'html.parser').find_all('div', {'id': 'ResponsiveTabs_6035'})[0].find_all(['p'])
    objectList = []
    for itemTotal in coursePage:
        objectList.append(itemTotal.text.splitlines())


    rquiredObj = []

    for objItem in objectList:
        rquiredObj.append(objItem)

    courseCode = course
    info=str()
    if courseCode is not None:
        for index, courseObj in enumerate(rquiredObj):
            if courseObj[0] != '':
                courseObj=courseObj[0].split()
                for l in courseObj:
                    if courseCode.upper() == l:
                        info=rquiredObj[index]+rquiredObj[index+1]+rquiredObj[index+2]+rquiredObj[index+3]
                        if len(info[3])<5:
                            info=info[:3]

                        return info
            else:
                courseObj=courseObj[1].split()
                for l in courseObj:
                    if courseCode.upper() == l:
                        info=rquiredObj[index]+rquiredObj[index+1]+rquiredObj[index+2]+rquiredObj[index+3]
                        info=info[1:]

                        return info

def searchCoursePetro(course):

    url = 'https://www.squ.edu.om/engineering/Academic/Undergraduate-Programs/Petroleum-and-Natural-Gas-Engineering'

    coursePage = BeautifulSoup(urlopen(url).read().decode('utf-8'), 'html.parser').find_all('div', {'id': 'ResponsiveTabs_6036'})[0].find_all(['p'])
    objectList = []
    for itemTotal in coursePage:
        objectList.append(itemTotal.text.splitlines())


    rquiredObj = []

    for objItem in objectList:
        rquiredObj.append(objItem)

    courseCode = course
    info=str()
    if courseCode is not None:
        for index, courseObj in enumerate(rquiredObj):
            if courseObj[0] != '':
                courseObj=courseObj[0].split()
                for l in courseObj:
                    if courseCode.upper() == l:
                        info=rquiredObj[index]+rquiredObj[index+1]+rquiredObj[index+2]+rquiredObj[index+3]
                        if len(info[3])<5:
                            info=info[:3]

                        return info
            else:
                courseObj=courseObj[1].split()
                for l in courseObj:
                    if courseCode.upper() == l:
                        info=rquiredObj[index]+rquiredObj[index+1]+rquiredObj[index+2]+rquiredObj[index+3]
                        info=info[1:]

                        return info
    


# print(searchCoursePetro("pnge4512"))