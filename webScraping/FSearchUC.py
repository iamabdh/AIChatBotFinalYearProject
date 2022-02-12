from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import unicodedata


mainUrl = "https://www.squ.edu.om/engineering/Faculty-and-Staff/"
url =  [
        "Deans-Office", "Department-of-Civil-and-Architectural-Engineering", 
        "Department-of-Electrical-and-Computer-Engineering", 
        "Department-of-Mechanical-and-Industrial-Engineering", 
        "Department-of-Petroleum-and-Chemical-Engineering", 
        "Mechatronics-Engineering-Program",
        "IT-Support"
        ]


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
  objNames = {}
  stuffPage = []
  for pages in url:
    stuffPage += bs(urlopen(mainUrl + pages).read().decode('utf-8'), 'html.parser').find_all('li')
  
  objectList = list()
  for itemTotal in stuffPage:
    objectList.append(itemTotal.text.splitlines())

  drName = [_name.lower() for _name in name.split()]


  drListCompared = {}
  for index, _drName in enumerate(objectList):
    for _item in _drName:
      _item = [item.lower() for item in _item.split()]
      nthMatched = len(list(set(drName) & set(_item)))
      if nthMatched >= 2:
          drListCompared[nthMatched] = [_drName]
          break   
      if  nthMatched >= 1:
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




  # add
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
            if'@' in indexEmail:
                email = index
                break

      objNames.update({
          pIndex : {
          'name'   :    str(pItem[0]),
          'role'   :   'Not listed'   if   roleNo == None else str(pItem[roleNo]),
          'roomNo' :   'Not listed'   if   roomNo == None else str(pItem[roomNo]),
          'Mobile' :   'Not listed'   if   mobileNo == None else str(pItem[mobileNo]),
          'email'  :   'Not listed'   if   email == None else str(pItem[email])      
          }
        })
  return objNames


print(searchFF("Ali"))



  





