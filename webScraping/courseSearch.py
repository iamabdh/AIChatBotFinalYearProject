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
    courseList = []
    if courseCode is not None:
        for index, courseObj in enumerate(rquiredObj):
            courseObj=courseObj[0].split()
            
            for l in courseObj:
                if courseCode.upper() == l:
                    info=rquiredObj[index]+rquiredObj[index+1]+rquiredObj[index+2]
                    
                    courseList.append(info)
                    break
    
    return {'Course Info: ': courseList}

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
    courseList = []
    if courseCode is not None:
        for index, courseObj in enumerate(rquiredObj):
            courseObj=courseObj[0].split()
            
            for l in courseObj:
                if courseCode.upper() == l:
                    info=rquiredObj[index]+rquiredObj[index+1]+rquiredObj[index+2]
                    
                    courseList.append(info)
                    break
def searchCourseCIVL(course):
    
    url = 'https://www.squ.edu.om/engineering/Academic/Undergraduate-Programs/-Civil-Engineering'

    coursePage = BeautifulSoup(urlopen(url).read().decode('utf-8'), 'lxml').find_all(['p'])
    objectList = []
    for itemTotal in coursePage:
        objectList.append(itemTotal.text.splitlines())


    rquiredObj = []

    for objItem in objectList:
        rquiredObj.append(objItem)

    courseCode = course
    courseList = []
    if courseCode is not None:
        for index, courseObj in enumerate(rquiredObj):
            courseObj=courseObj[0].split()
            
            for l in courseObj:
                if courseCode.upper() == l:
                    info=rquiredObj[index]+rquiredObj[index+1]+rquiredObj[index+2]
                    
                    courseList.append(info)
                    break        


    return courseList

y=input("Enter course code: ")

if (y[:4]=="ECCE")or(y[:4]=="ecce"):
    print(searchCourse(y))
# elif (y[:4]=="AREN")or(y[:4]=="aren"):
#     print(searchCourseArc(y))
# elif (y[:4]=="CIVL")or(y[:4]=="civl"):
#     print(searchCourseCIVL(y))

