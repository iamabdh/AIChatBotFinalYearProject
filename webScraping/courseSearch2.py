import mechanize
from bs4 import BeautifulSoup
import re


crName = ["ECCE","ecce","CIVL","civl","MEIE","meie","PNGE","pnge","MCTE","mcte","CHPE","chpe","AREN","aren","CAMS","cams","MASF","masf","ANVS","anvs","NREC","nrec","SWAE","swae","FSHN","fshn","PLNT","plnt","DEFE","defe","MUSC","musc","ARAB","arab","ENGL","engl","TRAN","tran","GEOG","geog","HIST","hist","THAR","thar","ARCH","arch","MASS","mass","TOUR","tour","PHIL","phil","SOCY","socy","SOWK","sowk","INFO","info","BCOM","bcom","ACCT","acct","IRSS","irss","POLS","pols","ECON","econ","FINA","fina","INFS","infs","POMG","pomg","STAT","stat","MRKT","mrkt","MNGT","mngt","TECH","tech","EDUC","educ","CUTM","cutm","PSYC","psyc","ISLM","islm","ARED","ared","ECED","eced","PHED","phed","ENGR","engr","CRLW","crlw","PULW","pulw","COLW","colw","PLLW","pllw","ICHS","ichs","MEDI","medi","MDLS","mdls","BIOC","bioc","IMMU","immu","MICR","micr","DRUG","drug","PHAR","phar","PHYL","phyl","MEDP","medp","EPIS","epis","HAEM","haem","GENT","gent","NURS","nurs","SCIE","scie","BIOL","biol","CHEM","chem","ERSC","ersc","GEOP","geop","COMP","comp","MATH","math","PHYS","phys","STAT","stat","FPCS","fpcs","FPMT","fpmt","FPEH","fpeh","FPEL","fpel","LANC","lanc","FPES","fpes","LANK","lank"]


def findAtrb(query):
  crNamePart = ""
  for code in query.split():
    if code in crName:
      crNamePart = code
      break
  crCodePart = re.findall('\d+', query)
  if crCodePart[0] and crNamePart:
    return searchCourse2(crNamePart + crCodePart[0])
  else:
    return {}

   
def searchCourse2(code) :  
    url = "https://portal.squ.edu.om/course-description"
    br = mechanize.Browser()
    br.set_handle_robots(False) # ignore robots
    br.open(url)
    br.select_form(nr=1)
    br["crscode"] = code
    res = br.submit()

    soup= BeautifulSoup(res.read().decode("utf-8"), "html.parser")
    try:
        course_html=soup.find_all('table')[1].find_all('span')
        course_html2=soup.find_all('table')[3].find_all('td')
        course_html3=soup.find_all('table')[2].find_all('td')
    except:
        return {
            
        }
    for index in range(0,len(course_html)):
                course_html[index]=course_html[index].text
    for index in range(0,len(course_html2)):
                course_html2[index]=course_html2[index].text
    for index in range(0,len(course_html3)):
                course_html3[index]=course_html3[index].text
    courseTitle=course_html[1][14:]
    courseCredits=course_html[2][7:]
    courseDescription=course_html2[0]
    PreRequisiteCourses=course_html3[0]
    

    return{
                    'CourseTitle'   :  'Not listed' if courseTitle==None else courseTitle,
                    'CourseCredits'   :   'Not listed' if courseCredits==None else courseCredits,
                    'PreRequisiteCourses' :  'Not listed' if PreRequisiteCourses==None else PreRequisiteCourses,
                    'CourseDescription' : 'Not listed' if courseDescription==None else courseDescription,      
           }