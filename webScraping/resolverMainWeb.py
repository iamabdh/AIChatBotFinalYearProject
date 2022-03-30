
# add directories for calling submodule
import os, sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)

class ResolverMainPage:
    def Guide():
        from webScraping import guide
        return guide.guide()

    def AboutPage():
        from webScraping import aboutPage
        return aboutPage.readAboutSQU()

    def FFSearch(name):
         from webScraping import FSearchUC
         if name is not None:
            listingName = name.split()
            listingName.remove(listingName[0])
            name = ' '.join(listingName)
         return FSearchUC.searchFF(name)
    
    def degreeSearch(yearDegree):
        from webScraping import degreePlanF
        if yearDegree is not None:
            listYeareDegree=yearDegree.split()
            year=listYeareDegree[0]
        return degreePlanF.degreePlan(year)
    def CourseSearch(name):
         from webScraping import courseSearch2
         listingName = name.split()
         listname=listingName[0]+listingName[1]
         
         return courseSearch2.searchCourse2(listname)
    
    def JobServices():
        from webScraping.Services import Services
        return Services.Job()
    def StaffServices():
         from webScraping.Services import Services
         return Services.StaffServices()
    def OnlineServices():
        from webScraping.Services import Services
        return Services.OnlineServices()

    def engineerECE():
        from webScraping.scrapingENG2 import Engineer
        return Engineer.electrical()

    def engineerCAE():
        from webScraping.scrapingENG2 import Engineer
        return Engineer.civilandArch()

    def engineerMIE():
        from webScraping.scrapingENG2 import Engineer
        return Engineer.MechanicalIndustrial()
    
    def engineerPCE():
        from webScraping.scrapingENG2 import Engineer
        return Engineer.PetroleumChemical()

    def engineerArch():
        from webScraping.scrapingENG2 import Engineer
        return Engineer.ArchEng()

    def engineerCivil():
        from webScraping.scrapingENG2 import Engineer
        return Engineer.CivilEng()
    def engineerMech():
        from webScraping.scrapingENG2 import Engineer
        return Engineer.MechEng()

    def engineerIndust():
        from webScraping.scrapingENG2 import Engineer
        return Engineer.IndustEng()

    def engineerMecatro():
        from webScraping.scrapingENG2 import Engineer
        return Engineer.MechatroEng()

    def engineerChem():
        from webScraping.scrapingENG2 import Engineer
        return Engineer.ChemEng()

    def engineerPetro():
        from webScraping.scrapingENG2 import Engineer
        return Engineer.PetroEng()
    def mainLibrary():
        from webScraping.libaryServices import Libraries
        return Libraries.MainLibrary()
    def OmaniLibrary():
        from webScraping.libaryServices import Libraries
        return Libraries.Omanilibrary()
    def Medicallibrary():
        from webScraping.libaryServices import Libraries
        return Libraries.Medicallibrary()
    def Educationlibrary():
        from webScraping.libaryServices import Libraries
        return Libraries.Educationlibrary()
    def Scienceslibrary():
        from webScraping.libaryServices import Libraries
        return Libraries.Scienceslibrary()
    def CEPSlibrary():
        from webScraping.libaryServices import Libraries
        return Libraries.CEPSlibrary()
    def Mosquelibrary():
        from webScraping.libaryServices import Libraries
        return Libraries.Mosquelibrary()
    def VisitorsInfo():
        from webScraping.hospital import Hospital
        return Hospital.VisitorsInfo()
    def PatientInfo():
        from webScraping.hospital import Hospital
        return Hospital.PatientInfo()


def resloverIntents(init, arg = None):
    if init == 'guide':
        return ResolverMainPage.Guide()
    elif init == 'AboutSQU':
        return ResolverMainPage.AboutPage()
    elif init == 'Electrical':
        return ResolverMainPage.engineerECE()
    elif init == 'CivilandArch':
        return ResolverMainPage.engineerCAE()
    elif init == 'CivilEngineering':
        return ResolverMainPage.engineerCivil()
    elif init == 'ArchEngineering':
        return ResolverMainPage.engineerArch()
    elif init == 'MechandIndus':
        return ResolverMainPage.engineerMIE()
    elif init == 'MechEngineering':
        return ResolverMainPage.engineerMech()
    elif init == 'IndustEngineering':
        return ResolverMainPage.engineerIndust()
    elif init == 'MechatroEngineering':
        return ResolverMainPage.engineerMecatro()
    elif init == 'Petr&Chem':
        return ResolverMainPage.engineerPCE()
    elif init == 'ChemEngineering':
        return ResolverMainPage.engineerChem()
    elif init == 'PetroEngineering':
        return ResolverMainPage.engineerPetro()
    elif init == 'searchFF':
        return  ResolverMainPage.FFSearch(arg)
    elif init == 'degreePlan':
        return  ResolverMainPage.degreeSearch(arg)
    elif init == "OnlineServices":
        return ResolverMainPage.OnlineServices() 
    elif init == "StaffServices":
        return ResolverMainPage.StaffServices()
    elif init == 'searchCourse':
        return  ResolverMainPage.CourseSearch(arg)
    elif init == "Job":
        return ResolverMainPage.JobServices()
    elif init == "MainLibrary":
        return ResolverMainPage.mainLibrary()   
    elif init == "Medicallibrary":
        return ResolverMainPage.Medicallibrary()
    elif init == "Omanilibrary":
        return ResolverMainPage.OmaniLibrary()
    elif init == "Scienceslibrary":
        return ResolverMainPage.Scienceslibrary()
    elif init == "CEPSlibrary":
        return ResolverMainPage.CEPSlibrary()
    elif init == "Educationlibrary":
        return ResolverMainPage.Educationlibrary()
    elif init == "Mosquelibrary":
        return ResolverMainPage.Mosquelibrary()
    elif init == "VisitorsInfo":
        return ResolverMainPage.VisitorsInfo()
    elif init == "PatientInfo":
        return ResolverMainPage.PatientInfo()
    else:
        return 0