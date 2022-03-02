# add directories for calling submodule
import os, sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import unicodedata
import datetime

def CheckDate(date):
    todayDate =  datetime.datetime.now()
    date = datetime.datetime.strptime(date, "%d-%m-%Y")
    if todayDate > date:
        return False
    else:
        return True


class Services:

    def StaffServices():
        url ="https://www.squ.edu.om/Staff"
        staffServicesPageHtml = bs(urlopen(url).read().decode("utf-8"), 
                           "html.parser").find_all('div', 
                                                   {
                                                       'id': 'dnn_ctr8120_View_Index_plLicense'
                                                    })[0].select(".accordion")[0].select(".accordion-item")


        staffServicesObject = {}


        for item in staffServicesPageHtml:
            staffServicesObject.update({
            str(item.select(".accordion-header")[0].text) : {
          "subText" : [str(item.select(".accordion-content")[0].text)]
                }
            })
        return staffServicesObject
    

    def OnlineServices():
        return {
        "Email" : {
            "forwordUrl" : "https://mail.squ.edu.om/"
        },
        "E-learning": {
            "forwordUrl" : "https://www.squ.edu.om/Student/E-learning"
        },

        "SIS": {
            "forwordUrl" : "https://sis.squ.edu.om/sis/webreg/3s/index.jsp"
        },
        "SQU Portal": {
            "forwordUrl" : "https://portal.squ.edu.om/"
        },
        "Changing Password": {
            "forwordUrl" : "https://uas.squ.edu.om/Home.aspx?lang=e"
            }
        }






    def Job():
        # JOBS
        JobData = {}

        for id in range(378, 500):

            JobURL = f"https://jobs.squ.edu.om/JobPositionDetails.aspx?jpid={id}"
            JobPageHtml = bs(urlopen(JobURL).read().decode("utf-8"), 
                                        "html.parser").find_all('div', 
                                                                {
                                                                    'class': 'main content-wrapper'
                                                                })[0].select(".container-fluid")[0].select(".row")[1].select(".col-sm-12")[0]
            print(id)
            categoryListJobInfos =  JobPageHtml.select(".alert")
            if not categoryListJobInfos:
                break
            else:
                if CheckDate(categoryListJobInfos[1].text):
                    categoryListCol = JobPageHtml.find_all("h3")[0].text
                    categoryListJob = JobPageHtml.find_all("h2")
                    if JobData.get(categoryListJob[0].text) is None:
                        JobData[categoryListJob[0].text] = {}
                    
                    JobData[categoryListJob[0].text].update({
                        id: {
                            "College" : categoryListCol,
                            "Department" : categoryListJob[1].text,
                            "Closing":  categoryListJobInfos[1].text,
                            "Qualification": categoryListJobInfos[5].text,
                            "Experience": categoryListJobInfos[4].text,
                            "Category": categoryListJobInfos[2].text,
                            "link": JobURL       
                        }})
                else:
                    continue

        return JobData   