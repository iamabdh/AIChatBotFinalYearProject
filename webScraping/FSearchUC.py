# add directories for calling submodule
import os, sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import unicodedata

listOfRole = [
    'Professor',
    'Associate Professor',
    'Assoc. Professor',
    'Assistant Professor',
    'Assitant  Professor',
    'Assitant', 'Professor',
    'Assoc.', 'Associate',
    'Lecturer', 'linguistics',
    'Department Superintendent',
    'Senior Engineer',
    'Lab Engineer',
    'IT Officer',
    'Technician (C)',
    'Engineer(B)',
    'Software Engineer',
    'Coordinator and follow up specialist',
    'Coordinator',
    'Visiting',
    'Faculty',
    "Superintendent", 
    "Senior",
    "Medical",
    "Lab",
    "Biomedical",
    "Chief", 
    "Head of Department",
    "Head", "Department", "Consultant", "medicine",
    "Specialist", "COORDINATOR", "House", "Social", "Psychologist", "Clinical", "Technologist", 
    "Science", "Hospital"

]


def handlingContent(tag, mainUrl, url, name):
    staffPages, objectList = list(), list()

    for pages in url:
        staffPages += bs(urlopen(mainUrl + pages).read().decode('utf-8'), 'html.parser').find_all(tag)

    for itemTotal in staffPages:
        objectList.append(itemTotal.text.splitlines())

    drName = [_name.lower() for _name in name.split()]

    drListCompared = {}
    for index, _drName in enumerate(objectList):
        for _item in _drName:
            _item = [item.lower() for item in _item.split()]
            nthMatched = len(list(set(drName) & set(_item)))
            if nthMatched >= len(drName):
                if nthMatched not in drListCompared:
                    drListCompared[nthMatched] = [_drName]
                else:
                    if _drName not in drListCompared[nthMatched]:
                        drListCompared[nthMatched].append(_drName)
                    else:
                        continue

    try:
        # only takes heighest value of key
        drListNames = drListCompared[max(drListCompared)]
    except:
        return 0

    for index, item in enumerate(drListNames):
        _list = []
        for _item in item:
            _list.append(unicodedata.normalize("NFKD", _item))

        while '' in _list:
            _list.remove('')
        while ' ' in _list:
            _list.remove(' ')

        drListNames[index] = _list

    return drListNames


def Eng(name):
    objNames = {}
    mainUrl = "https://www.squ.edu.om/engineering/Faculty-and-Staff/"
    url = [
        "Deans-Office", "Department-of-Civil-and-Architectural-Engineering",
        "Department-of-Electrical-and-Computer-Engineering",
        "Department-of-Mechanical-and-Industrial-Engineering",
        "Department-of-Petroleum-and-Chemical-Engineering",
        "Mechatronics-Engineering-Program",
        "IT-Support"
    ]

    drListNames = handlingContent('li', mainUrl, url, name)
    if not drListNames:
        return
    for pIndex, pItem in enumerate(drListNames):
        roleNo = None
        roomNo = None
        email = None
        mobileNo = None

        for index, item in enumerate(pItem):

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
                if '+' != str(pItem[mobileNo])[0]:
                    mobileNo = None
            for indexEmail in item:
                if '@' in indexEmail:
                    email = index
                    break

        objNames.update({
            pIndex: {
                'name': str(pItem[0]),
                'role': 'Not listed' if roleNo == None else str(pItem[roleNo]),
                'room': 'Not listed' if roomNo == None else str(pItem[roomNo]),
                'mobile': 'Not listed' if mobileNo == None else str(pItem[mobileNo]),
                'email': 'Not listed' if email == None else str(pItem[email])
            }
        })
    return objNames


def Sec(name):
    objNames = {}
    mainUrl = "https://www.squ.edu.om/science/Departments/"

    url = [
        "Biology/People",
        "Chemistry/People",
        "Computer-Science/Department-People/Faculty",
        "Earth-Sciences/Staff",
        "Mathematics/People",
        "Physics/People",
        "Statistics/People"
    ]

    drListNames = handlingContent('tr', mainUrl, url, name)
    if not drListNames:
        return
    for pIndex, pItem in enumerate(drListNames):
        roleNo = None
        roomNo = None
        email = None
        mobileNo = None

        for index, item in enumerate(pItem):
            if "Title:" in item:
                splitTitle = item.split(":")[-1].strip()
                if len(list(set(listOfRole) & set(splitTitle.split()))) > 0:
                    roleNo = splitTitle

            # check its Room No.
            if 'Office No.' in item:
                roomNo = item.split(".")[-1].strip()
            if 'Mobile Telephone No.' in item:
                mobileNo = index + 1
                if '+' != str(pItem[mobileNo])[0]:
                    mobileNo = None
            for indexEmail in item:
                if '@' in indexEmail:
                    email = item.split(":")[-1].strip()
                    break
        objNames.update({
            pIndex: {
                'name': str(pItem[0]),
                'role': 'Not listed' if roleNo == None else roleNo,
                'room': 'Not listed' if roomNo == None else roomNo,
                'mobile': 'Not listed' if mobileNo == None else str(pItem[mobileNo]),
                'email': 'Not listed' if email == None else email
            }
        })
    return objNames


def Art(name):
    objNames = {}
    mainUrl = "https://www.squ.edu.om/art/Departments/"

    url = [
        "Theater-Art/Department-Staff",
        "Arabic-Language-and-Literature/Department-Staff",
        "Archaeology/Department-Staff",
        "English-Language-and-Literature/Department-Staff",
        "Geography/Department-Staff",
        "History/Department-Staff",
        "Information-Studies/Department-Staff",
        "Mass-Communication/Department-Staff",
        "Music-and-Musicology/Department-Staff",
        "Sociology-Social-Work/Department-Staff",
        "Tourism/Department-Staff"
    ]

    drListNames = handlingContent("tr", mainUrl, url, name)
    if not drListNames:
        return
    for pIndex, pItem in enumerate(drListNames):
        roleNo = None
        roomNo = None
        email = None
        mobileNo = None

        for index, item in enumerate(pItem):

            if len(list(set(listOfRole) & set(item.split()))) > 0:
                roleNo = item.strip()

            # check its Room No.
            if 'Office' in item:
                roomNo = item.split(".")[-1].strip().split(":")[-1].strip()

            if 'Mobile Telephone No.' in item:
                mobileNo = index + 1
                if '+' != str(pItem[mobileNo])[0]:
                    mobileNo = None
            for indexEmail in item:
                if '@' in indexEmail:
                    email = item.split(":")[-1].strip()
                    break
        objNames.update({
            pIndex: {
                'name': str(pItem[0]),
                'role': 'Not listed' if roleNo == None else roleNo,
                'room': 'Not listed' if roomNo == None else roomNo,
                'mobile': 'Not listed' if mobileNo == None else str(pItem[mobileNo]),
                'email': 'Not listed' if email == None else email
            }
        })
    return objNames


def Eco(name):
    objNames = {}

    mainUrl = "https://www.squ.edu.om/economics/Departments/"
    url = [
        "Accounting/Faculty-and-Staff",
        "Business-Communication-Unit/Faculty-and-Staff",
        "Economics-and-Finance/Faculty-and-Staff",
        "Information-System/Faculty-and-Staff",
        "Management/Faculty-and-Staff",
        "Marketing/Faculty-and-Staff",
        "Operation-Management-Business-statics/Faculty-and-Staff",
        "Political-Science/Faculty-and-Staff"
    ]
    drListNames = handlingContent('tr', mainUrl, url, name)
    if not drListNames:
        return
    for pIndex, pItem in enumerate(drListNames):
        roleNo = None
        roomNo = None
        email = None
        mobileNo = None

        for index, item in enumerate(pItem):
            if "Title:" in item:
                splitTitle = item.split(":")[-1].strip()
                if len(list(set(listOfRole) & set(splitTitle.split()))) > 0:
                    roleNo = splitTitle

            # check its Room No.
            if 'Office No.' in item:
                roomNo = item.split(".")[-1].strip()
            if 'Mobile Telephone No.' in item:
                mobileNo = index + 1
                if '+' != str(pItem[mobileNo])[0]:
                    mobileNo = None
            for indexEmail in item:
                if '@' in indexEmail:
                    email = item.split(":")[-1].strip()
                    break
        objNames.update({
            pIndex: {
                'name': str(pItem[0]),
                'role': 'Not listed' if roleNo == None else roleNo,
                'room': 'Not listed' if roomNo == None else roomNo,
                'mobile': 'Not listed' if mobileNo == None else str(pItem[mobileNo]),
                'email': 'Not listed' if email == None else email
            }
        })
    return objNames

def Med(name):
    objNames = {}

    mainUrl = "https://www.squ.edu.om/medicine/Staff-directory/"
    url = [
        "Allied-Health-Sciences-Department-staff",
        "Anesthesia-and-Intensive-care-Department-staff",
        "Behavioral-Medicine-Department-staff",
        "Biochemistry-Department-staff",
        "Child-Health-Department-staff",
        "Family-Medicine-and-Public-Health-Department-staff",
        "Genetics-Department-staff",
        "Human-Clinical-Anatomy-Department-staff",
        "Medical-Education-Informatics-Department-staff",
        "Obstetrics-Gynecology-Department-staff",
        "Ophthalmology-Department-staff",
        "Pathology-Department-staff",
        "Pharmacology-Clinical-Pharmacy-Department-staff",
        "Physiology-Department-staff",
        "Radiology-Molecular-Imaging-Department-staff",
        "Surgery-Department-staff"

    ]
    drListNames = handlingContent('tr', mainUrl, url, name)
    if not drListNames:
        return 0
    for pIndex, pItem in enumerate(drListNames):
        roleNo = None
        roomNo = None
        email = None
        mobileNo = None

        for index, item in enumerate(pItem):
            if "Title:" in item:
                splitTitle = item.split(":")[-1].strip()
                if len(list(set(listOfRole) & set(splitTitle.split()))) > 0:
                    roleNo = splitTitle

            # check its Room No.
            if 'Office No.' in item:
                roomNo = item.split(".")[-1].strip()
            if 'Mobile Telephone No.' in item:
                mobileNo = index + 1
                if '+' != str(pItem[mobileNo])[0]:
                    mobileNo = None
            for indexEmail in item:
                if '@' in indexEmail:
                    email = item.split(":")[-1].strip()
                    break
        objNames.update({
            pIndex: {
                'name': str(pItem[0]),
                'role': 'Not listed' if roleNo == None else roleNo,
                'roomNo': 'Not listed' if roomNo == None else roomNo,
                'Mobile': 'Not listed' if mobileNo == None else str(pItem[mobileNo]),
                'email': 'Not listed' if email == None else email
            }
        })
    return objNames



def searchFF(name, content=None):
    objNamesTotal = {}
    engSearch = Eng(name)
    secSearch = Sec(name)
    artSearch = Art(name)
    ecoSearch = Eco(name)
    medSearch = Med(name)
    if engSearch is not None:
        objNamesTotal['College of Engineering'] = engSearch
    if secSearch is not None:
        objNamesTotal['College of Science'] = secSearch
    if artSearch is not None:
        objNamesTotal['College Of Art'] = artSearch
    if ecoSearch is not None:
        objNamesTotal['College Of Economic'] = ecoSearch
    if medSearch is not None:
        objNamesTotal['College of Medicine and Health Sciences'] = medSearch

    if objNamesTotal:
        return objNamesTotal
    return 0
