# add directories for calling submodule
import os, sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)




from bs4 import BeautifulSoup
from urllib.request import urlopen
import unicodedata



listOfRole = ['Professor', 
'Associate Professor', 
'Assoc. Professor', 
'Assistant Professor',
'Assitant  Professor',
'Lecturer',
'Department Superintendent',
'Senior Engineer',
'Lab Engineer',
'IT Officer',
'Technician (C)', 
'Engineer(B)',
'Software Engineer',
'Coordinator and follow up specialist',
'Coordinator']



def searchFF(name):
    url = 'https://www.squ.edu.om/engineering/Faculty-and-Staff/Department-of-Electrical-and-Computer-Engineering'

    stuffPage = BeautifulSoup(urlopen(url).read().decode('utf-8'), 'lxml').find_all('li')

    objectList = []
    for itemTotal in stuffPage:
        objectList.append(itemTotal.text.splitlines())


    rquiredObj = []

    for objItem in objectList:
        rquiredObj.append(objItem)

    drName = name
    drnameList = []
    if drName is not None:
        for index, DrNameObj in enumerate(rquiredObj):
            for l in DrNameObj:
                if drName.lower() == l.lower():
                    drnameList.append(DrNameObj)
                    break

  
        
    newList = []
    try: 
        for item in drnameList[0]:
            newList.append(unicodedata.normalize("NFKD",item))
    except: 
        return 0

    # remove white empty string in list
    while '' in newList:
        newList.remove('')
    while ' ' in newList:
        newList.remove(' ')
    roleNo = None
    roomNo = None
    email = None
    mobileNo = None
    for index, item in enumerate(newList):
        # checking the role of required Dr name
        itemSP = item.split(",")
        
        #  checking there Role in Dept.

        if len(list(set(listOfRole) & set(itemSP))) > 0:
            roleNo = index
        
        # check its Room No.
        if 'Room No.' in item:
            roomNo = index + 1
        if 'Mobile Telephone No.' in item:
          mobileNo = index + 1
          if '+' != str(newList[mobileNo])[0]:
            mobileNo = None
        for indexEmail in item:
            if'@' in indexEmail:
                email = index
                break

    if newList is not None:
        if newList[0] is not None:
           return{
                    'name'   :    str(newList[0]),
                    'role'   :   'Not listed'   if   roleNo == None else str(newList[roleNo]),
                    'roomNo' :   'Not listed'   if   roomNo == None else str(newList[roomNo]),
                    'Mobile' :   'Not listed'   if   mobileNo == None else str(newList[mobileNo]),
                    'email'  :   'Not listed'   if   email == None else str(newList[email])
           }
    else:
        return 0