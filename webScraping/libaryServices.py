
import os, sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)

from email.headerregistry import Address
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Libraries():
    
    def MainLibrary():
        mainlibrary ={}

        pageLibraryVisionMissionValues = urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/Main-Library/Library-Vision-Mission-and-Values') 
        html = pageLibraryVisionMissionValues.read().decode('utf-8')
        mainlibary_html = BeautifulSoup(html, "html.parser")
        SQUParagragh_html = mainlibary_html.find_all('div',{'id':'dnn_ctr3726_HtmlModule_lblContent'})[0]
        lib_htm1=SQUParagragh_html.find_all('p')

        introduction=''

        for i in lib_htm1[1:6]:
            introduction +=f'{i.text}'
        


        Vision=''
        for i in lib_htm1[7:9]:
            Vision +=f'{i.text}'
        


        mission=''
        for i in lib_htm1[9:12]:
            mission +=f'{i.text}'
        

        
        valuIntroduction=''
        for i in lib_htm1[12:14]:
            valuIntroduction +=f'{i.text}'
        


        valuepoint=SQUParagragh_html.find_all('ul')[0].find_all('li')
        objectivepoint=SQUParagragh_html.find_all('ul')[2].find_all('li')

        value = list() # list = []
        for  item in valuepoint:
            value.append(item.text)
        

        
        objectiveintroduction=''
        for i in lib_htm1[16:17]:
            objectiveintroduction +=f'{i.text}'
        

        objctive=list()
        for item in objectivepoint:
            objctive.append(item.text)
        

        mainlibrary.update({
            "introdctionmivi" :{
                "subText" : [str(introduction)]
            },
            "Vission":{
                "subText":[str(Vision)]
            },
            "Mission":{
                "subText":[str(mission)]
            },
            "value Introduction":{
                "subText":[str(valuIntroduction)]
          
            },
            "value":{
                "subText" : [],
                "extend": value
            },
            "objective introduction":{
                "subText":[str(objectiveintroduction)]
            },
            "objective":{
                "subText": [],
                "extend":objctive
            },
        })
###
        pageMainLibraryCodeofConduct= urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/Main-Library/Code-of-Conduct') 
        html2 = pageMainLibraryCodeofConduct.read().decode('utf-8')
        libarySQU_html = BeautifulSoup(html2, "html.parser")
        SQUParagragh_html = libarySQU_html.find_all('div',{'id':'dnn_ctr9678_HtmlModule_lblContent'})[0]
        libary_htm1=SQUParagragh_html.find_all('p')
        libaryintro=libary_htm1[0].text
        libaryusers=SQUParagragh_html.find_all('ul')[0].find_all('li')    
        libarystaf=SQUParagragh_html.find_all('ul')[1].find_all('li')   

        
        
        users=list()
        for item in libaryusers:
            users.append(item.text)
          
        
        
        
        staff=list()
        for item in libarystaf:
            staff.append(item.text)   
        

        mainlibrary.update({
                "libary introduction" :{
                     "subText" : [str(libaryintro)]
                 
                },
                "library users":{
                    "subText": [],
                    "extend":users
                },
                "libraey staff":{
                    "subText": [],
                    "extend":staff
                },
                
            })
        
        # 
        pageDirectionsMaps= urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/Main-Library/Directions-Maps') 
        html3 = pageDirectionsMaps.read().decode('utf-8')
        Directionslibary_html = BeautifulSoup(html3, "html.parser")
        directions = Directionslibary_html.find_all('div',{'id':'dnn_ctr3757_ContentPane'})[0]
        Di=directions.find_all('p')
        all_text1=str()
        for text1 in Di:
            all_text1 += text1.text +'\n'

        
                
        mainlibrary.update({
                "direction" :{
                     "subText" : [str(all_text1)]
                 },
             })
######
        pagemainContactUs = urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/Main-Library/Library-Contacts') 
        html4 = pagemainContactUs.read().decode('utf-8')
        contmainlibary_html = BeautifulSoup(html4, "html.parser")
        contucs_html = contmainlibary_html.find_all('div',{'id':'dnn_ctr3813_HtmlModule_lblContent'})[0]
        contactUS=contucs_html.find_all('p')[1].text
        
                
        mainlibrary.update({
                "Contacts" :{
                     "subText" : [str(contactUS)]
                        
                 },
            
         })

        return mainlibrary


    def Medicallibrary(): 
        medicallibrary ={}
        pagemediMissionVisionandObjectives = urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/Medical-Library/Library-Mission-Vision-and-Objectives') 
        html5 = pagemediMissionVisionandObjectives.read().decode('utf-8')
        medicallibary_html = BeautifulSoup(html5, "html.parser")
        SQUParagragh_html = medicallibary_html.find_all('div',{'id':'dnn_ctr7212_HtmlModule_lblContent'})[0]
        lib_htm1=SQUParagragh_html.find_all('p')
        
        over1=lib_htm1[0].text
        over2=lib_htm1[1].text
        over3=lib_htm1[2].text
        Overview=over1+over2+over3
       
        
    
        vision1=lib_htm1[3].text
        
        mission1=lib_htm1[5].text
        
        objective1=SQUParagragh_html.find_all('ul')[3].text
        
        medicallibrary.update({
                "Overview" :{
                     "subText" : [str(Overview)]
                 },
                
                "vision1":{
                    "subText":[str(vision1)]
                },
                "mission1":{
                    "subText":[str(mission1)]
                },
                "objective1":{
                    "subText":[str(objective1)]
                },
            })
    
        pagemedicContactUs = urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/Medical-Library/Library-Contacts') 
        html6 = pagemedicContactUs.read().decode('utf-8')
        contMedlibary_html = BeautifulSoup(html6, "html.parser")
        contuctMedical = contMedlibary_html.find_all('div',{'id':'dnn_ctr7511_HtmlModule_lblContent'})[0]
        ContucsUs1=contuctMedical.find_all('p')
        all_text2=str()
        for text1 in ContucsUs1:
            all_text2 += text1.text +'\n'

        
        medicallibrary.update({
                "medicalcontacts" :{
                     "subText" : [str(all_text2)]
                 },
        })
        
        pageUsefulLinks = urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/Medical-Library/Useful-Links') 
        html7 = pageUsefulLinks.read().decode('utf-8')
        usefullink = BeautifulSoup(html7, "html.parser")
        useful = usefullink.find_all('div',{'id':'dnn_ctr7512_ContentPane'})[0]
        link=useful.find_all('p')
        li=useful.find_all('li') 
        Useful=list()
        for item in li:
            Useful.append(item.text)
        
        
        medicallibrary.update({
                "usefullink" :{
                     "subText" : [],
                     "extend":Useful
                 },
        })
        return medicallibrary




    def Omanilibrary(): 
        omanilibrary ={}
        pageOmaniStudiesCenterLibrary = urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/Omani-Studies-Center-Library/About-OSC-Library') 
        html8 = pageOmaniStudiesCenterLibrary.read().decode('utf-8')
        OmaniStudiesCenterLibrary= BeautifulSoup(html8, "html.parser")
        CenterLibrary= OmaniStudiesCenterLibrary.find_all('div',{'id':'dnn_TopPane'})[0]
        librarycenter=CenterLibrary.find_all('p')
        introcent1=librarycenter[1].text
        introcent2=librarycenter[2].text
        introcent3=librarycenter[5].text  
        
        introcuctonCenter=introcent1+introcent2+introcent3
        Objectiveslibrary=CenterLibrary.find_all('ul')[0].find_all('li')
        objectiveslibrary=list()
        for item in Objectiveslibrary:
            objectiveslibrary.append(item.text)

        bulding=''

        for i in librarycenter[8:20]:
            bulding +=f'{i.text}'
        
        omanilibrary.update({
                "introcucton Center" :{
                     "subText" : [str(introcuctonCenter)]
                     
                },
                "objectives library":{
                    "subText":[],
                    "extend":objectiveslibrary
                },
                "bulding":{
                    "subText":[str(bulding)]
                },
                
            }) 
            
        pageLibraryPolicies = urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/Omani-Studies-Center-Library/Library-Policies') 
        html9 = pageLibraryPolicies.read().decode('utf-8')
        LibraryPolicies= BeautifulSoup(html9, "html.parser")
        libpolic=LibraryPolicies.find_all('div',{'id':'dnn_ctr7824_ContentPane'})[0]
        librarycenter=libpolic.find_all('p')
        all_text3=str()
        for text1 in librarycenter:
            all_text3 += text1.text +'\n'

        omanilibrary.update({
                "library policies" :{
                     "subText" : [str(all_text3)]
                 },
        })
        
        pageLibraryServices = urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/Omani-Studies-Center-Library/Library-Services') 
        html10 = pageLibraryServices.read().decode('utf-8')
        LibraryServices= BeautifulSoup(html10, "html.parser")
        libserv=LibraryServices.find_all('div',{'id':'dnn_ctr7825_HtmlModule_lblContent'})[0]
        libhtm1=libserv.find_all('p')
        CirculationService=libhtm1[1].text
        
        CirculationA=libserv.find_all('ul')[0].find_all('li')
        Cir=list()
        for item in CirculationA:
            Cir.append(item.text)
        CirculationR=libserv.find_all('ul')[1].find_all('li')   
        Circ=list()
        for item in CirculationR:
            Circ.append(item.text)
        
        ReferenceService=''

        for i in libhtm1[2:10]:
            ReferenceService +=f'{i.text}'
         
        Computers=libhtm1[10].text
        
        computerwirles=libserv.find_all('ul')[2].find_all('li')
        Com=list()
        for item in computerwirles:
            Com.append(item.text)
        
        IntroductoryTour=''

        for i in libhtm1[11:20]:
            IntroductoryTour +=f'{i.text}'
         
        Rules=libserv.find_all('ul')[3].find_all('li')
        r=list()
        for item in Rules:
            r.append(item.text)

        omanilibrary.update({
                "Circulation Service" :{
                     "subText" : [str(CirculationService)]
                 },
                "Circulation is available for":{
                    "subText":[],
                    "extend":Cir
                 },
                 "Circulation rules":{
                    "subText":[],
                    "extend":Circ
                 },
                "Reference Service":{
                     "subText":[str(ReferenceService)]
                },
                "Computers":{
                    "subText":[str(Computers)]
                },
                "computer wirles":{
                "subText":[],
                "extend":Com
                },
                "Introductory Tours":{
                "subText":[str(IntroductoryTour)]
                },
                "rules":{
                "subText":[],
                "extend":r
                },
                
            }) 

        pageUsefullink= urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/Omani-Studies-Center-Library/Useful-Links')
        html12 = pageUsefullink.read().decode('utf-8')
        Libraryuselink= BeautifulSoup(html12, "html.parser")
        libuselink=Libraryuselink.find_all('div',{'id':'dnn_ctr7827_HtmlModule_lblContent'})[0]
        libhtm1uselink=libuselink.find_all('p')

        all_text5=str()
        for text1 in libhtm1uselink:
            all_text5 += text1.text +'\n'

        omanilibrary.update({
                "useful links" :{
                     "subText" : [str(all_text5)]
                 },
        })
        
        pageAskLibrarian = urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/Omani-Studies-Center-Library/Ask-a-Librarian')
        html13 = pageAskLibrarian.read().decode('utf-8')
        Asklib= BeautifulSoup(html13, "html.parser")
        libraryask=Asklib.find_all('div',{'id':'dnn_ctr7829_ContentPane'})[0]
        libhtm1ask=libraryask.find_all('p')

        all_text6=str()
        for text1 in libhtm1ask:
            all_text6 += text1.text +'\n'
            print(all_text6)
        omanilibrary.update({
                "Ask a Librarian" :{
                     "subText" : [str(all_text6)]
                 },
        })
        return omanilibrary



    def Scienceslibrary(): 
        scienceslibrar ={}
        pageAbouttheLibrary= urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/College-of-Art-Social-Sciences-Library/About-Library')
        html14 = pageAbouttheLibrary.read().decode('utf-8')
        Aboutlibrary= BeautifulSoup(html14, "html.parser")
        libraryAbout =Aboutlibrary.find_all('div',{'id':'dnn_ctr7831_HtmlModule_lblContent'})[0]
        libhtm1about=libraryAbout.find_all('p')

        all_text7=str()
        for text1 in libhtm1about:
            all_text7 += text1.text +'\n'
           
            scienceslibrar.update({
                "About the library" :{
                     "subText" : [str(all_text7)]
                 },

            })


###

        pagescienceslibrary= urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/College-of-Art-Social-Sciences-Library/Library-Mission-and-Objectives')
        html15 = pagescienceslibrary.read().decode('utf-8')
        libmissobjec= BeautifulSoup(html15, "html.parser")
        Sociolsciences =libmissobjec.find_all('div',{'id':'dnn_ctr7832_HtmlModule_lblContent'})[0]
        libhtm1limisob=Sociolsciences.find_all('p')
        libaryobj=Sociolsciences.find_all('ul')[0].find_all('li')    
        MissionObject=''

        for i in libhtm1limisob[1:6]:
            MissionObject +=f'{i.text}'
        

        LibraryObjactives=list()
        for item in libaryobj:
            LibraryObjactives.append(item.text)
        
        LibraryObjact=''

        for i in libhtm1limisob[6:20]:
            LibraryObjact +=f'{i.text}'
        
        scienceslibrar.update({
                "library mission" :{
                     "subText" : [str(MissionObject)]
                 },
                     "Library Objactives" :{
                     "subText" : [],
                     "extend":LibraryObjactives
                 },
                     "library objactive" :{
                     "subText" : [str(LibraryObjact)]
                 
                 },

            })

###
        pageInformationServices = urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/College-of-Art-Social-Sciences-Library/Information-Services') 
        html16 = pageInformationServices.read().decode('utf-8')
        informationSQU_html = BeautifulSoup(html16, "html.parser")
        informserv =informationSQU_html.find_all('div',{'id':'dnn_ctr7833_HtmlModule_lblContent'})[0]
        libhtm1inform=informserv.find_all('p')

        all_text8=str()
        for text1 in libhtm1inform:
            all_text8 += text1.text +'\n'
            
        scienceslibrar.update({
                "Information Services" :{
                     "subText" : [str(all_text8)]
                 },
        })
###

        pageBorrowingPolicy = urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/College-of-Art-Social-Sciences-Library/Information-Services/Borrowing-Policy') 
        html17 = pageBorrowingPolicy.read().decode('utf-8')
        BorrowSQU_html = BeautifulSoup(html17, "html.parser")
        Borrowing =BorrowSQU_html.find_all('div',{'id':'dnn_ctr7834_HtmlModule_lblContent'})[0]
        libhtm1Borrow=Borrowing.find_all('p')

        book=Borrowing.find_all('ul')[0].find_all('li')
        introductionborrow=''
        for i in libhtm1Borrow[0:9]:
            introductionborrow +=f'{i.text}'
        

        Books=list()
        for item in book:
            Books.append(item.text)
        

        reference=Borrowing.find_all('ul')[1].find_all('li')
        Reference=list()
        for item in reference:
            Reference.append(item.text)
    

        journal=Borrowing.find_all('ul')[2].find_all('li')
        Journals=list()
        for item in journal:
            Journals.append(item.text)
            
        scienceslibrar.update({
                "introduction borrow" :{
                     "subText" : [str(introductionborrow)]
                 },
                     "Books" :{
                     "subText" : [],
                     "extend":Books
                 },
                     
                     "Reference" :{
                     "subText" : [],
                     "extend":Reference
                 },
                     " Journals" :{
                     "subText" : [],
                     "extend": Journals
                 
                 },

            })
###

        pageArtAbouttheLibraryy= urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/College-of-Art-Social-Sciences-Library/Information-Software') 
        html18 = pageArtAbouttheLibraryy.read().decode('utf-8')
        BorrowingSoftwarSQU_html = BeautifulSoup(html18, "html.parser")
        BorrowingSoftware =BorrowingSoftwarSQU_html.find_all('div',{'id':'dnn_ctr7835_ContentPane'})[0]
        libhtm1Soft=BorrowingSoftware.find_all('p')
        all_text9=str()
        for text1 in libhtm1Soft:
            all_text9 += text1.text +'\n'

        scienceslibrar.update({
                "the borrowing software:" :{
                     "subText" : [str(all_text9)]
                 },
        })

###
        pageLibraryStaffDirectory = urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/College-of-Art-Social-Sciences-Library/Library-Staff-Directory') 
        html19 = pageLibraryStaffDirectory.read().decode('utf-8')
        staffSQU_html = BeautifulSoup(html19, "html.parser")
        staffdirectory =staffSQU_html.find_all('div',{'id':'dnn_ctr7836_HtmlModule_lblContent'})[0]
        libhtm1staff=staffdirectory.find_all('p')
        all_text10=str()
        for text1 in libhtm1staff:
            all_text10 += text1.text +'\n'
            
        scienceslibrar.update({
                "library staff directory" :{
                     "subText" : [str(all_text10)]
                 },
        })


###

        pageArtLibraryContacts= urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/College-of-Art-Social-Sciences-Library/Library-Contacts') 
        html20 = pageArtLibraryContacts.read().decode('utf-8')
        contactsSQU_html = BeautifulSoup(html20, "html.parser")
        libcontac =contactsSQU_html.find_all('div',{'id':'dnn_ctr7837_HtmlModule_lblContent'})[0]
        libhtm1cont=libcontac.find_all('p')
        all_text11=str()
        for text1 in libhtm1cont:
            all_text11 += text1.text +'\n'

        
        scienceslibrar.update({
                "library contacts of art" :{
                     "subText" : [str(all_text11)]
                 },
        })
        return scienceslibrar




    def Educationlibrary():
        educationlibrary ={}

        pageEducationLibrary = urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/College-of-Education-Library/Library-Vision-Mission-and-Values') 
        html21 = pageEducationLibrary.read().decode('utf-8')
        LVMVSQU_html = BeautifulSoup(html21, "html.parser")
        libraryLVMV =LVMVSQU_html.find_all('div',{'id':'dnn_ctr7840_HtmlModule_lblContent'})[0]
        libhtm1VMV=libraryLVMV.find_all('p')

        OBjective=libraryLVMV.find_all('li')[3:9]
        VISIon=libhtm1VMV[0].text
        LibMis=libhtm1VMV[1].text

        ObJeC=list()
        for item in OBjective:
            ObJeC.append(item.text)
            
        educationlibrary.update({
            "Vission of education library" :{
                "subText" : [str(VISIon)]
            },
            "Mission of education library":{
                "subText":[str(LibMis)]
            
            },
            "objective of education library":{
                "subText" : [],
                "extend": ObJeC
                 },
        })
####

        pageeducationlibraryservices = urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/College-of-Education-Library/Library-Services') 
        html22 = pageeducationlibraryservices.read().decode('utf-8')
        servlib = BeautifulSoup(html22, "html.parser")
        SQUlibrarser_html = servlib.find_all('div',{'id':'dnn_ctr7841_ContentPane'})[0]
        lib_htm1ser=SQUlibrarser_html.find_all('p')

        LiSe1=lib_htm1ser[0].text
        LiSe2=lib_htm1ser[2].text
        LiSe3=lib_htm1ser[8].text

        LiSe4=lib_htm1ser[11].text

        LiSe5=lib_htm1ser[12].text


        LiSe6=lib_htm1ser[13].text


        LiSe7=lib_htm1ser[14].text

        LiSe8=lib_htm1ser[16].text

        LiSe9=lib_htm1ser[17].text

        LiSe10=lib_htm1ser[18].text

        LiSe11=lib_htm1ser[19].text
        

        educationlibrary.update({
            "introduction of library Service" :{
                "subText" : [str(LiSe1)]
            },
            "Loan Service":{
                "subText":[str(LiSe2)]
            },
            "References and information service":{
                "subText":[str(LiSe3)]
            },
            "Printed Book":{
                "subText":[str(LiSe4)]
          
            },
             
            "E-book":{
                "subText":[str(LiSe5)]
          
            }, 
            "Electronic Periodicals":{
                "subText":[str(LiSe6)]
          
            }, 
            "Databases":{
                "subText":[str(LiSe7)]
          
            },
            "Photocopy and reproduction service":{
                "subText":[str(LiSe8)]
          
            },
            "Computers and Internet service":{
                "subText":[str(LiSe9)]
          
            },
            "Current Awareness Service":{
                "subText":[str(LiSe10)]
          
            },
            "Other services":{
                "subText":[str(LiSe11)]
          
            },
        })

###
        pageeducationContactUs = urlopen('https://www.squ.edu.om/libraries/SQU-Libraries/College-of-Education-Library/Library-Contacts') 
        html23 = pageeducationContactUs.read().decode('utf-8')
        EdLiCo = BeautifulSoup(html23, "html.parser")
        SQUlibcont_html = EdLiCo.find_all('div',{'id':'dnn_ctr7842_ContentPane'})[0]
        lib_htm1conta=SQUlibcont_html.find_all('p')
        all_text12=str()
        for text1 in lib_htm1conta:
            all_text12 += text1.text +'\n'

            
        educationlibrary.update({
            "education library contacs us" :{
                "subText" : [str(all_text12)]
            },
        })
        return educationlibrary





