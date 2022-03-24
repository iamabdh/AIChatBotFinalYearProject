import mechanize
from bs4 import BeautifulSoup
   
def searchCourse2(code) :  
    url = "https://portal.squ.edu.om/course-description"
    br = mechanize.Browser()
    br.set_handle_robots(False) # ignore robots
    br.open(url)
    br.select_form(nr=1)
    br["crscode"] = code
    res = br.submit()

    soup= BeautifulSoup(res.read().decode("utf-8"), "html.parser")
    course_html=soup.find_all('table')[1].find_all('span')
    course_html2=soup.find_all('table')[3].find_all('td')
    course_html3=soup.find_all('table')[2].find_all('td')
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
