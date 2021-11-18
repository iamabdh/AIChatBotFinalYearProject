# add directories for calling submodule
import os, sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)



# Read SQU main page and resolve the request in object format
# The object requested as model from tensorflow equation 



from urllib.request import urlopen
from bs4 import BeautifulSoup

# Requested url that will get html pages 
url = 'https://www.squ.edu.om/'

class Engineer():
    
    def electrical():
        aboutElectricl={}
        # extract with id content in engeineering About page
        page13 = urlopen(url + 'engineering/About/Departments/Electrical-and-Computer-Engineering/Welcome-Message') 
        html13 = page13.read().decode('utf-8')
        ECEwelcom_html = BeautifulSoup(html13, "html.parser")
        ECEwelcomParagragh_html = ECEwelcom_html.find_all('div', {'id': 'dnn_ctr5864_HtmlModule_lblContent'})
        ECEwelcom_text = ECEwelcomParagragh_html[0].text.strip().split("   ")[0]
        
        # store every infos in aboutObj
        aboutElectricl.update({
            "ECEwelcom" : {
                "subText" : [str(ECEwelcom_text)],
        }
     })

        page14 = urlopen(url + 'engineering/About/Departments/Electrical-and-Computer-Engineering/Vision-and-Mission') 
        html14 = page14.read().decode('utf-8')
        ECE_VM_html = BeautifulSoup(html14, "html.parser")
        ECE_VMParagragh_html = ECE_VM_html.find_all('div', {'id': 'dnn_ctr5866_HtmlModule_lblContent'})
        ECE_VM_titles = ECE_VMParagragh_html[0].find_all('strong')
        ECE_VM_subText = ECE_VMParagragh_html[0].find_all('p')
        ECE_VM_extends = ECE_VMParagragh_html[0].find_all('li')
        # print(ECE_VM_extends.text)
        # exit(1)
        for index in range(0,len(ECE_VM_extends)):
            ECE_VM_extends[index]=ECE_VM_extends[index].text

        aboutElectricl.update({
            "VisionElectrical":{
                "subText":[str(ECE_VM_subText[1].text)]
            },
            "missionElectrical":{
                "subText":[str(ECE_VM_subText[4].text)]
            },
            "objectivesElectrical":{
                "subText":[],
                "extend":ECE_VM_extends
            },

        })
        page15 = urlopen(url + 'engineering/About/Departments/Electrical-and-Computer-Engineering/Quality-Assurance') 
        html15 = page15.read().decode('utf-8')
        ECE_QA_html = BeautifulSoup(html15, "html.parser")
        ECE_QAParagragh_html = ECE_QA_html.find_all('div', {'id': 'dnn_ctr5867_HtmlModule_lblContent'})
        ECE_QA_subText = ECE_QAParagragh_html[0].text.strip().split("   ")[0]
        
        aboutElectricl.update({
            "QualityAssuranceElectrical" : {
            "subText" : [str(ECE_QA_subText)],
        }
     })
       
        page16 = urlopen(url + 'engineering/About/Departments/Electrical-and-Computer-Engineering/Industrial-Advisory-Board') 
        html16 = page16.read().decode('utf-8')
        ECE_IAB_html = BeautifulSoup(html16, "html.parser")
        ECE_IABParagragh_html = ECE_IAB_html.find_all('div', {'id': 'dnn_ctr5868_HtmlModule_lblContent'})
        ECE_IAB_subtext = ECE_IABParagragh_html[0].find_all('p')
        ECE_IAB_extend = ECE_IABParagragh_html[0].find_all('li')
        
        for index in range(0,len(ECE_IAB_extend)):
            ECE_IAB_extend[index]=ECE_IAB_extend[index].text

        aboutElectricl.update({
            "Industrial Advisory Board Electrical":{
                "subText":[str(ECE_IAB_subtext[0].text),str(ECE_IAB_subtext[1].text)],
            },
            "Advisory Board Responsibilities Electrical":{
                "subText":[],
                "extend":str(ECE_IAB_extend)
            }
            
        })

        return aboutElectricl
    
    def civilandArch():
        aboutCivilandArch={}
        page9 = urlopen(url + 'engineering/About/Departments/Civil-and-Architectural-Engineering/Welcome-Message') 
        html9 = page9.read().decode('utf-8')
        CAEwelcom_html = BeautifulSoup(html9, "html.parser")
        CAEwelcomParagragh_html = CAEwelcom_html.find_all('div', {'id': 'dnn_ctr5749_HtmlModule_lblContent'})
        CAEwelcom_text = CAEwelcomParagragh_html[0].text.strip().split("   ")[0]
        
        # store every infos in aboutObj
        aboutCivilandArch.update({
            "CAEwlcome" : {
                "subText" : [str(CAEwelcom_text)],
        }
     })

        page10 = urlopen(url + 'engineering/About/Departments/Civil-and-Architectural-Engineering/Vision-and-Mission') 
        html10 = page10.read().decode('utf-8')
        CAE_VM_html = BeautifulSoup(html10, "html.parser")
        CAE_VMParagragh_html = CAE_VM_html.find_all('div', {'id':'dnn_ctr5750_HtmlModule_lblContent'})
        CAE_VM_subText = CAE_VMParagragh_html[0].find_all('p')
        CAE_VM_extends = CAE_VMParagragh_html[0].find_all('li')

        for index in range(0,len(CAE_VM_extends)):
            CAE_VM_extends[index]=CAE_VM_extends[index].text

        aboutCivilandArch.update({
            "VisionCivil-and-Architectural-Engineering":{
                "subText":[str(CAE_VM_subText[0].text)]
            },
            "missionCivil-and-Architectural-Engineering":{
                "subText":[str(CAE_VM_subText[2].text)],
                "extend":CAE_VM_extends
            },
        })
        page11 = urlopen(url + 'engineering/About/Departments/Civil-and-Architectural-Engineering/Quality-Assurance') 
        html11 = page11.read().decode('utf-8')
        CAE_QA_html = BeautifulSoup(html11, "html.parser")
        CAE_QAParagragh_html = CAE_QA_html.find_all('div', {'id': 'dnn_ctr5752_HtmlModule_lblContent'})
        CAE_QA_subText = CAE_QAParagragh_html[0].text.strip().split("   ")[0]
        
        aboutCivilandArch.update({
            "QualityAssurance Civil-and-Architectural-Engineering" : {
            "subText" : [str(CAE_QA_subText)],
        }
     })

        page12 = urlopen(url + 'engineering/About/Departments/Civil-and-Architectural-Engineering/Industrial-Advisory-Board') 
        html12 = page12.read().decode('utf-8')
        CAE_IAB_html = BeautifulSoup(html12, "html.parser")
        CAE_IABParagragh_html = CAE_IAB_html.find_all('div', {'id':  'dnn_ctr5754_HtmlModule_lblContent'})
        CAE_IAB_subtext = CAE_IABParagragh_html[0].find_all('p')
        CAE_IAB_extend = CAE_IABParagragh_html[0].find_all('li')
        
        for index in range(0,len(CAE_IAB_extend)):
            CAE_IAB_extend[index]=CAE_IAB_extend[index].text

        aboutCivilandArch.update({
            "Industrial Advisory Board Civil-and-Architectura":{
                "subText":[str(CAE_IAB_subtext[0].text)+str(CAE_IAB_subtext[1].text)],
            },
            
        })
        return aboutCivilandArch

    def MechanicalIndustrial():
        aboutMechanicalandIndustrial={}
        page17 = urlopen(url + 'engineering/About/Departments/Mechanical-and-Industrial-Engineering/Welcome-Message') 
        html17 = page17.read().decode('utf-8')
        MIEwelcom_html = BeautifulSoup(html17, "html.parser")
        MIEwelcomParagragh_html = MIEwelcom_html.find_all('div', {'id': 'dnn_ctr5869_HtmlModule_lblContent'})
        MIEwelcom_text = MIEwelcomParagragh_html[0].find_all('p')
        MIEwelcom_text=MIEwelcom_text[2].text
        
        
        aboutMechanicalandIndustrial.update({
            "MIEwlcome" : {
                "subText" : [str(MIEwelcom_text)],
        }
        })
        page18 = urlopen(url + 'engineering/About/Departments/Mechanical-and-Industrial-Engineering/Vision-and-Mission') 
        html18 = page18.read().decode('utf-8')
        MIE_VM_html = BeautifulSoup(html18, "html.parser")
        MIE_VMParagragh_html = MIE_VM_html.find_all('div', {'id': 'dnn_ctr5971_HtmlModule_lblContent'})
        MIE_VM_subText = MIE_VMParagragh_html[0].find_all('p')
        MIE_VM_extends = MIE_VMParagragh_html[0].find_all('li')
        

        for index in range(0,len(MIE_VM_extends)):
            MIE_VM_extends[index]=MIE_VM_extends[index].text

        aboutMechanicalandIndustrial.update({
            "VisionMechanical-and-Industrial":{
                "subText":[str(MIE_VM_subText[1].text)]
            },
            "missionMechanical-and-Industrial":{
                "subText":[str(MIE_VM_subText[4].text)],
                "extend":MIE_VM_extends
            },
        })
        page19 = urlopen(url + 'engineering/About/Departments/Mechanical-and-Industrial-Engineering/Quality-Assurance') 
        html19 = page19.read().decode('utf-8')
        MIE_QA_html = BeautifulSoup(html19, "html.parser")
        MIE_QAParagragh_html = MIE_QA_html.find_all('div', {'id': 'dnn_ctr5972_HtmlModule_lblContent'})[0].find_all(['p','li','span']) 
        MIE_QA_subText = MIE_QAParagragh_html[0].text.strip().split("   ")[0]
        
        aboutMechanicalandIndustrial.update({
            "QualityAssurance Mechanical-and-Industrial-Engineering" : {
            "subText" : [str(MIE_QA_subText)],
        }
     })

        page20 = urlopen(url + 'engineering/About/Departments/Mechanical-and-Industrial-Engineering/Industrial-Advisory-Board') 
        html20 = page20.read().decode('utf-8')
        MIE_IAB_html = BeautifulSoup(html20, "html.parser")
        MIE_IABParagragh_html = MIE_IAB_html.find_all('div', {'id': 'dnn_ctr5973_ModuleContent'})
        MIE_IAB_subtext = MIE_IABParagragh_html[0].find_all('p')
        MIE_IAB_extend = MIE_IABParagragh_html[0].find_all('li')
        
        for index in range(0,len(MIE_IAB_extend)):
            MIE_IAB_extend[index]=MIE_IAB_extend[index].text

        aboutMechanicalandIndustrial.update({
            "Industrial Advisory Board Mechanical-and-Industrial":{
                "subText":[str(MIE_IAB_subtext[0].text)],
                "extend":str(MIE_IAB_extend)
            }
            
        })

        return aboutMechanicalandIndustrial

    def PetroleumChemical():
        aboutPetroleumChemical={}
        page21 = urlopen(url + 'engineering/About/Departments/Petroleum-and-Chemical-Engineering/Welcome-Message') 
        html21 = page21.read().decode('utf-8')
        PCEwelcom_html = BeautifulSoup(html21, "html.parser")
        PCEwelcomParagragh_html = PCEwelcom_html.find_all('div', {'id': 'dnn_ctr5974_ModuleContent'}) 
        PCEwelcom_text = PCEwelcomParagragh_html[0].find_all('p')
        PCEwelcom_text=PCEwelcom_text[2].text+PCEwelcom_text[4].text+PCEwelcom_text[6].text
        
        
        aboutPetroleumChemical.update({
            "PCEwlcome" : {
                "subText" : [str(PCEwelcom_text)],
        }
     })

        page22 = urlopen(url + 'engineering/About/Departments/Petroleum-and-Chemical-Engineering/Vision-and-Mission') 
        html22 = page22.read().decode('utf-8')
        PCE_VM_html = BeautifulSoup(html22, "html.parser")
        PCE_VMParagragh_html = PCE_VM_html.find_all('div', {'id': 'dnn_ctr5975_ContentPane'})
        PCE_VM_subText = PCE_VMParagragh_html[0].find_all('p')
        MIE_VM_extends = PCE_VMParagragh_html[0].find_all('li')
        

        for index in range(0,len(MIE_VM_extends)):
            MIE_VM_extends[index]=MIE_VM_extends[index].text

        aboutPetroleumChemical.update({
            "VisionPetroleum-and-Chemical":{
                "subText":[str(PCE_VM_subText[1].text)]
            },
            "missionPetroleum-and-Chemical":{
                "subText":[str(PCE_VM_subText[3].text),str(PCE_VM_subText[4].text)],
                "extend":MIE_VM_extends
            },
        })

        page23 = urlopen(url + 'engineering/About/Departments/Petroleum-and-Chemical-Engineering/Quality-Assurance') 
        html23 = page23.read().decode('utf-8')
        PCE_QA_html = BeautifulSoup(html23, "html.parser")
        PCE_QAParagragh_html = PCE_QA_html.find_all('div', {'id': 'dnn_ctr5978_ContentPane'})
        PCE_QA_subText = PCE_QAParagragh_html[0].text.strip().split("   ")[0]
        
        aboutPetroleumChemical.update({
            "QualityAssurance Petroleum-and-Chemical" : {
            "subText" : [str(PCE_QA_subText)],
            }
        })

        page24 = urlopen(url + 'engineering/About/Departments/Petroleum-and-Chemical-Engineering/Industrial-Advisory-Board') 
        html24 = page24.read().decode('utf-8')
        PCE_IAB_html = BeautifulSoup(html24, "html.parser")
        PCE_IABParagragh_html = PCE_IAB_html.find_all('div', {'id': 'dnn_ctr5979_ModuleContent'})
        PCE_IAB_subtext = PCE_IABParagragh_html[0].find_all('p')

        aboutPetroleumChemical.update({
            "Industrial Advisory Board Petroleum-and-Chemical":{
                "subText":[str(PCE_IAB_subtext[0].text),str(PCE_IAB_subtext[1].text)],
                "extend":[]
            }
            
        })



        return aboutPetroleumChemical
