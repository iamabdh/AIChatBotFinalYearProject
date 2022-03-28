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
            "ECE welcom" : {
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
            "Vision Electrical":{
                "subText":[str(ECE_VM_subText[1].text)]
            },
            "Mission Electrical":{
                "subText":[str(ECE_VM_subText[4].text)]
            },
            "Objectives Electrical":{
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
            "Quality Assurance Electrical" : {
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
                "extend": ECE_IAB_extend
            }
            
        })
        page100= urlopen(url + 'engineering/Academic/Undergraduate-Programs/Electrical-and-Computer-Engineering')
        html100 = page100.read().decode('utf-8')
        ECE_About_html = BeautifulSoup(html100, "html.parser")
        ECE_AboutParagragh_html = ECE_About_html.find_all('div', {'id': 'ResponsiveTabs_6031'})
        ECE_About = ECE_AboutParagragh_html[0].find_all('p')
        ECE_About_subtext=ECE_About[0].text +ECE_About[2].text
        commonCourseECE=ECE_About[29].text
        CSPcourse=ECE_About[32].text
        CSNcourse=ECE_About[35].text
        EICcourse=ECE_About[38].text
        PSEcourse=ECE_About[41].text
        trainCourse=ECE_About[44].text
        ECE_About_outcomes = ECE_AboutParagragh_html[0].find_all('li')[7:14]
        for index in range(0,len(ECE_About_outcomes)):
            ECE_About_outcomes[index]=ECE_About_outcomes[index].text
        

        aboutElectricl.update({
            "About ECE":{
                "subText":[ECE_About_subtext],
            },
            "Common Courses ECE":{
                "subText":[commonCourseECE],
        
            },
            "CSP Courses":{
                "subText":[CSPcourse],
            },
            "CSN Courses":{
                "subText":[CSNcourse],
            },
            "EIC Courses":{
                "subText":[EICcourse],
            },
            "PSE Courses":{
                "subText":[PSEcourse],
            },
            
            "Train Course":{
                "subText":[trainCourse],
            }, 
            "Outcomes Of ECE Students":{
                "subText":ECE_About_outcomes,
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
            "CAE Wlcome" : {
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
            "Vision Civil and Architectural Engineering":{
                "subText":[str(CAE_VM_subText[0].text)]
            },
            "Mission Civil and Architectural Engineering":{
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
            "Quality Assurance Civil and Architectural Engineering" : {
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
            "Industrial Advisory Board Civil and Architectura":{
                "subText":[str(CAE_IAB_subtext[0].text), str(CAE_IAB_subtext[1].text)],
            },
            
        })
        
        return aboutCivilandArch
    def CivilEng():
        aboutCivil={}
        page100= urlopen(url + 'engineering/Academic/Undergraduate-Programs/-Civil-Engineering')
        html100 = page100.read().decode('utf-8')
        CAE_About_html = BeautifulSoup(html100, "html.parser")
        CAE_AboutParagragh_html = CAE_About_html.find_all('div', {'id': 'ResponsiveTabs_6029'})
        CAE_About = CAE_AboutParagragh_html[0].find_all('p')
        CAE_AboutOverview=CAE_About[0].text
        CAEcommonCourses=CAE_About[26].text
        civilSpecialCoreses=CAE_About[29].text
        civilTraining=CAE_About[32].text
        civilOutcomes = CAE_AboutParagragh_html[0].find_all('li')[6:9]
        for index in range(0,len(civilOutcomes)):
            civilOutcomes[index]=civilOutcomes[index].text
        aboutCivil.update({
            "Civil Engineering Overview":{
                "subText":[CAE_AboutOverview]
            },
            "Civil Engineering Common Courses":{
                "subText":[CAEcommonCourses],
                "extend":[]
            },
            "Civil Engineering Special Courses":{
                "subText":[civilSpecialCoreses],
                "extend":[]
            },
            "Civil Engineering Training":{
                "subText":[civilTraining],
                "extend":[]
            },
            "Civil Engineering Outcomes":{
                "subText":civilOutcomes,
                "extend":[]
            },
        })
        return aboutCivil
    def ArchEng():
        ArchObject={}
        page100= urlopen(url + 'engineering/Academic/Undergraduate-Programs/Architectural-Engineering')
        html100 = page100.read().decode('utf-8')
        Arch_About_html = BeautifulSoup(html100, "html.parser")
        Arch_Paragragh_html = Arch_About_html.find_all('div', {'id': 'ResponsiveTabs_6024'})
        Arch_About = Arch_Paragragh_html[0].find_all('p')
        ArchText=Arch_About[0].text
        ArchCommonCourses=Arch_About[28].text
        ArchSpecialCourses=Arch_About[31].text
        ArchTrainingCourse=Arch_About[34].text
        ArchOutcomes=Arch_About[37].text+Arch_About[38].text+Arch_About[39].text
        ArchObject.update({
            "Architectural Engineering Overview":{
                "subText":[ArchText]
            },
            "Architectural Engineering CommonCourses":{
                "subText":[ArchCommonCourses],
                "extend":[]
            },
            "Architectural Engineering SpecialCourses":{
                "subText":[ArchSpecialCourses],
                "extend":[]
            },
            "Architectural Engineering Training":{
                "subText":[ArchTrainingCourse],
                "extend":[]
            },
            "Architectural Engineering Outcomes":{
                "subText":[ArchOutcomes],
                "extend":[]
            },

        })





        return ArchObject
    def MechEng():
        Mechobject={}

        page100= urlopen(url + 'engineering/Academic/Undergraduate-Programs/Mechanical-Engineering')
        html100 = page100.read().decode('utf-8')
        Mech_About_html = BeautifulSoup(html100, "html.parser")
        Mech_Paragragh_html = Mech_About_html.find_all('div', {'id': 'ResponsiveTabs_6033'})
        Mech_About = Mech_Paragragh_html[0].find_all('p')
        Mech_text=Mech_About[0].text+Mech_About[1].text+Mech_About[2].text
        MechCommonCourses=Mech_About[29].text
        MechSpecialCourses=Mech_About[32].text
        MechTrainingCourse=Mech_About[35].text
        MechOutcomes=Mech_Paragragh_html[0].find_all('li')[6:11]
        for index in range(0,len(MechOutcomes)):
            MechOutcomes[index]=MechOutcomes[index].text
        Mechobject.update({
            "Mechanical Engineering Overview":{
                "subText":[Mech_text]
            },
            "Mechanical Engineering Common Courses":{
                "subText":[MechCommonCourses],
                "extend":[]
            },
            "Mechanical Engineering Special Courses":{
                "subText":[MechSpecialCourses],
                "extend":[]
            },
            "Mechanical Engineering Training":{
                "subText":[MechTrainingCourse],
                "extend":[]
            },
            "Mechanical Engineering Outcomes":{
                "subText":MechOutcomes,
                "extend":[]
            },
        })

        return Mechobject

    def IndustEng():
        Industobject={}

        page100= urlopen(url + 'engineering/Academic/Undergraduate-Programs/Industrial-Engineering')
        html100 = page100.read().decode('utf-8')
        Indust_About_html = BeautifulSoup(html100, "html.parser")
        Indust_Paragragh_html = Indust_About_html.find_all('div', {'id': 'ResponsiveTabs_6032'})
        Indust_About = Indust_Paragragh_html[0].find_all('p')
        Indust_text=Indust_About[0].text+Indust_About[1].text+Indust_About[2].text
        IndustCommonCourses=Indust_About[28].text
        IndustSpecialCourses=Indust_About[31].text
        IndustTrainingCourse=Indust_About[34].text
        IndustOutcomes=Indust_Paragragh_html[0].find_all('li')[6:11]
        for index in range(0,len(IndustOutcomes)):
            IndustOutcomes[index]=IndustOutcomes[index].text

        Industobject.update({
            "Industerial Engineering Overview":{
                "subText":[Indust_text]
            },
            "Industerial Engineering Common Courses":{
                "subText":[IndustCommonCourses],
                "extend":[]
            },
            "Industerial Engineering Special Courses":{
                "subText":[IndustSpecialCourses],
                "extend":[]
            },
            "Industerial Engineering Training":{
                "subText":[IndustTrainingCourse],
                "extend":[]
            },
            "Industerial Engineering Outcomes":{
                "subText":IndustOutcomes,
                "extend":[]
            },
        })

        return Industobject

    def MechanicalIndustrial():
        aboutMechanicalandIndustrial={}
        page17 = urlopen(url + 'engineering/About/Departments/Mechanical-and-Industrial-Engineering/Welcome-Message') 
        html17 = page17.read().decode('utf-8')
        MIEwelcom_html = BeautifulSoup(html17, "html.parser")
        MIEwelcomParagragh_html = MIEwelcom_html.find_all('div', {'id': 'dnn_ctr5869_HtmlModule_lblContent'})
        MIEwelcom_text = MIEwelcomParagragh_html[0].find_all('p')
        MIEwelcom_text=MIEwelcom_text[2].text
        
        
        aboutMechanicalandIndustrial.update({
            "MIE Wlcome" : {
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
            "Vision Mechanical and Industrial":{
                "subText":[str(MIE_VM_subText[1].text)]
            },
            "Mission Mechanical and Industrial":{
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
            "Quality Assurance Mechanical and Industrial Engineering" : {
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
            "Industrial Advisory Board Mechanical and Industrial":{
                "subText":[str(MIE_IAB_subtext[0].text)],
                "extend":str(MIE_IAB_extend)
            }
            
        })

        return aboutMechanicalandIndustrial
    def MechatroEng():
        Mechatroobject={}

        page100= urlopen(url + 'engineering/Academic/Undergraduate-Programs/Mechatronics-Engineering')
        html100 = page100.read().decode('utf-8')
        Mechatro_About_html = BeautifulSoup(html100, "html.parser")
        Mechatro_Paragragh_html = Mechatro_About_html.find_all('div', {'id': 'ResponsiveTabs_6034'})
        Mechatro_About = Mechatro_Paragragh_html[0].find_all('p')
        Mechatro_text=Mechatro_About[0].text
        MechatroCommonCourses=Mechatro_About[27].text
        MechatroSpecialCourses=Mechatro_About[31].text
        MechatroTrainingCourse=Mechatro_About[34].text
        MechatroOutcomes=Mechatro_Paragragh_html[0].find_all('li')[6:9]
        for index in range(0,len(MechatroOutcomes)):
            MechatroOutcomes[index]=MechatroOutcomes[index].text


        Mechatroobject.update({
            "Mechatronics Engineering Overview":{
                "subText":[Mechatro_text]
            },
            "Mechatronics Engineering Common Courses":{
                "subText":[MechatroCommonCourses],
                "extend":[]
            },
            "Mechatronics Engineering Special Courses":{
                "subText":[MechatroSpecialCourses],
                "extend":[]
            },
            "Mechatronics Engineering Training":{
                "subText":[MechatroTrainingCourse],
                "extend":[]
            },
            "Mechatronics Engineering Outcomes":{
                "subText":MechatroOutcomes,
                "extend":[]
            },
        })

        return Mechatroobject

    def ChemEng():
        ChemObject={}
        page100= urlopen(url + 'engineering/Academic/Undergraduate-Programs/Chemical-and-Process-Engineering')
        html100 = page100.read().decode('utf-8')
        Chem_About_html = BeautifulSoup(html100, "html.parser")
        Chem_Paragragh_html = Chem_About_html.find_all('div', {'id': 'ResponsiveTabs_6035'})
        Chem_About = Chem_Paragragh_html[0].find_all('p')
        ChemText=Chem_About[0].text
        ChemCommonCourses=Chem_About[26].text
        ChemSpecialCourses=Chem_About[29].text
        ChemTrainingCourse=Chem_About[32].text
        ChemOutcomes=Chem_Paragragh_html[0].find_all('li')[5:8]
        for index in range(0,len(ChemOutcomes)):
            ChemOutcomes[index]=ChemOutcomes[index].text

        ChemObject.update({
            "Chemical Engineering Overview":{
                "subText":[ChemText]
            },
            "Chemical Engineering Common Courses":{
                "subText":[ChemCommonCourses],
                "extend":[]
            },
            "Chemical Engineering Special Courses":{
                "subText":[ChemSpecialCourses],
                "extend":[]
            },
            "Chemical Engineering Training":{
                "subText":[ChemTrainingCourse],
                "extend":[]
            },
            "Chemical Engineering Outcomes":{
                "subText":ChemOutcomes,
                "extend":[]
            },

        })


        return ChemObject

    def PetroEng():
        PetroObject={}
        page100= urlopen(url + 'engineering/Academic/Undergraduate-Programs/Petroleum-and-Natural-Gas-Engineering')
        html100 = page100.read().decode('utf-8')
        Petro_About_html = BeautifulSoup(html100, "html.parser")
        Petro_Paragragh_html = Petro_About_html.find_all('div', {'id': 'ResponsiveTabs_6036'})
        Petro_About = Petro_Paragragh_html[0].find_all('p')
        PetroText=Petro_About[0].text
        PetroCommonCourses=Petro_About[27].text
        PetroSpecialCourses=Petro_About[31].text
        PetroTrainingCourse=Petro_About[33].text
        PetroOutcomes=Petro_Paragragh_html[0].find_all('li')[5:8]
        for index in range(0,len(PetroOutcomes)):
            PetroOutcomes[index]=PetroOutcomes[index].text

        PetroObject.update({
            "Petroleum Engineering Overview":{
                "subText":[PetroText]
            },
            "Petroleum Engineering Common Courses":{
                "subText":[PetroCommonCourses],
                "extend":[]
            },
            "Petroleum Engineering Special Courses":{
                "subText":[PetroSpecialCourses],
                "extend":[]
            },
            "Petroleum Engineering Training":{
                "subText":[PetroTrainingCourse],
                "extend":[]
            },
            "Petroleum Engineering Outcomes":{
                "subText":PetroOutcomes,
                "extend":[]
            },

        })


        return PetroObject

    def PetroleumChemical():
        aboutPetroleumChemical={}
        page21 = urlopen(url + 'engineering/About/Departments/Petroleum-and-Chemical-Engineering/Welcome-Message') 
        html21 = page21.read().decode('utf-8')
        PCEwelcom_html = BeautifulSoup(html21, "html.parser")
        PCEwelcomParagragh_html = PCEwelcom_html.find_all('div', {'id': 'dnn_ctr5974_ModuleContent'}) 
        PCEwelcom_text = PCEwelcomParagragh_html[0].find_all('p')
        PCEwelcom_text=PCEwelcom_text[2].text+PCEwelcom_text[4].text+PCEwelcom_text[6].text
        
        
        aboutPetroleumChemical.update({
            "PCE Wlcome" : {
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
            "Vision Petroleum and Chemical":{
                "subText":[str(PCE_VM_subText[1].text)]
            },
            "Mission Petroleum and Chemical":{
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
            "QualityAssurance Petroleum and Chemical" : {
            "subText" : [str(PCE_QA_subText)],
            }
        })

        page24 = urlopen(url + 'engineering/About/Departments/Petroleum-and-Chemical-Engineering/Industrial-Advisory-Board') 
        html24 = page24.read().decode('utf-8')
        PCE_IAB_html = BeautifulSoup(html24, "html.parser")
        PCE_IABParagragh_html = PCE_IAB_html.find_all('div', {'id': 'dnn_ctr5979_ModuleContent'})
        PCE_IAB_subtext = PCE_IABParagragh_html[0].find_all('p')

        aboutPetroleumChemical.update({
            "Industrial Advisory Board Petroleum and Chemical":{
                "subText":[str(PCE_IAB_subtext[0].text),str(PCE_IAB_subtext[1].text)],
                "extend":[]
            }
            
        })



        return aboutPetroleumChemical
