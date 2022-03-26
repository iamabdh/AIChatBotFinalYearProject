
import os, sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)

from email.headerregistry import Address
from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs


class Hospital():
    
    def VisitorsInfo():
        visitorsinfo={}
        url5 = "https://www.squ.edu.om/squh/Patients-Visitors/Visitors-Info/Visiting-Hours"
        openingHourHtml5 = bs(urlopen(url5).read().decode("utf-8"), "html.parser").find_all('table')[0].find_all('tr')


        firsTable5=openingHourHtml5[1].find_all('td')
        thirdTable5=openingHourHtml5[2].find_all('td')
        secondTable5=openingHourHtml5[3].find_all('td')
        fourTable5=openingHourHtml5[4].find_all('td')



        openingHour5 = str()

        for index, item in enumerate(firsTable5):
          if index == 0:
            openingHour5 +=item.text +": "
          elif index == len(firsTable5) - 1:
            openingHour5 += item.text + "\n"
          else:
            openingHour5 += item.text + " "
        for index, item in enumerate(thirdTable5):
          if index == 0:
            openingHour5 +=item.text +": "
          elif index == len(thirdTable5) - 1:
            openingHour5 += item.text + "\n"
          else:
            openingHour5 += item.text + " "     
        for index, item in enumerate(secondTable5):
          if index == 0:
            openingHour5 +=item.text +": "
          elif index == len(secondTable5) - 1:
            openingHour5 += item.text + "\n"
          else:
            openingHour5 += item.text + " "
        for index, item in enumerate(fourTable5):
          if index == 0:
            openingHour5 +=item.text +": "
          elif index == len(fourTable5) - 1:
            openingHour5 += item.text + "\n"
          else:
            openingHour5 += item.text + " "     


        ffirst=openingHourHtml5[7].find_all('td')
        firsTable5=openingHourHtml5[8].find_all('td')
        thirdTable5=openingHourHtml5[9].find_all('td')
        secondTable5=openingHourHtml5[3].find_all('td')


        openingHour6 = str()
        for index, item in enumerate(ffirst):
          if index == 0:
            openingHour6 +=item.text +": "
          elif index == len(ffirst) - 1:
            openingHour6 += item.text + "\n"
          if index == 0:
            openingHour6 +=item.text +": "
        for index, item in enumerate(firsTable5):
          if index == 0:
            openingHour6 +=item.text +": "
          elif index == len(firsTable5) - 1:
            openingHour6 += item.text + "\n"
          if index == 0:
             openingHour6 +=item.text +": "
        for index, item in enumerate(thirdTable5):
          if index == 0:
            openingHour6 +=item.text +": "
          elif index == len(thirdTable5) - 1:
            openingHour6 += item.text + "\n"
          else:
            openingHour6 += item.text + " "     

        openingHour7 = str()
        firsTable7=openingHourHtml5[12].find_all('tr')
        for index, item in enumerate(firsTable7):
          if index == 0:
            openingHour7 =item.text +": "
          elif index == len(firsTable7) -1:
            openingHour7 += item.text + "\n"
          if index == 0:
            openingHour7 =item.text +": "

        opvisitors=openingHour5+ "\n"+openingHour6+ "\n"+openingHour7
        
                
        visitorsinfo.update({
                "visitors table" :{
                     "subText" : [str(opvisitors)]
                        
                 },
        })
#######################
        url66 = "https://www.squ.edu.om/squh/Patients-Visitors/Visitors-Info/Visiting-Hours/Pharmacy"
        openingHourHtml66 = bs(urlopen(url66).read().decode("utf-8"), "html.parser").find_all('table')[0].find_all('tr')


        firsTablePharmacy=openingHourHtml66[0].find_all('tr')



        openingHour11 = str()

        for index, item in enumerate(firsTablePharmacy):
          if index == 0:
            openingHour11 +=item.text +": "
          elif index == len(firsTablePharmacy) - 1:
            openingHour11 += item.text + "\n"
          else:
            openingHour11 += item.text + " "


        secondTablepramcy=openingHourHtml66[6].find_all('tr')



        openingHour12 = str()

        for index, item in enumerate(secondTablepramcy):
          if index == 0:
            openingHour12 =item.text +": "
          elif index == len(secondTablepramcy) :
            openingHour12 += item.text + "\n"
          else:
            openingHour12 += item.text + " "


        thirdparamcy=openingHourHtml66[11].find_all('tr')



        openingHour13 = str()

        for index, item in enumerate(thirdparamcy):
          if index == 0:
            openingHour13 =item.text +": "
          elif index == len(thirdparamcy) :
            openingHour13 += item.text + "\n"
          else:
            openingHour13 += item.text + " "


        paramcyhour=openingHour11+openingHour12+openingHour13
        visitorsinfo.update({
                "paramcy table" :{
                     "subText" : [str(paramcyhour)]
                        
                 },
            
         })

        return visitorsinfo
        
###################
    def PatientInfo():
        patientinfo={}
        pagebirthcertificate= urlopen('https://www.squ.edu.om/squh/Patients-Visitors/Patient-Info/Birth-Death-Certificate') 
        birthcertificatehtml = pagebirthcertificate.read().decode('utf-8')
        libary_html = BeautifulSoup(birthcertificatehtml, "html.parser")
        birthcertificate_html = libary_html.find_all('div',{'id':'dnn_ctr3778_ContentPane'})[0]

        birth_htm1=birthcertificate_html.find_all('p')

        all_text000=str()
        for text1 in birth_htm1:
          all_text000 += text1.text
        
        deathcertificate_html = libary_html.find_all('div',{'id':'dnn_ctr5815_ContentPane'})[0]

        dith_htm1=deathcertificate_html.find_all('p')

        all_text00=str()
        for text1 in dith_htm1:
          all_text00 += text1.text

        print(all_text00)
        patientinfo.update({
                "Procedures to get a birth certificate" :{
                     "subText" : [str(all_text000)]
                        
                 },
                "Procedures to get death certificate" :{
                     "subText" : [str(all_text00)]
                        
                 },
            
         })

        return patientinfo