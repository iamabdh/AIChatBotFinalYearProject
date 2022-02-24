
# add directories for calling submodule
import os, sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)

class ResolverMainPage:

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





def resloverIntents(int, arg = None):

    if int == 'AboutSQU':
        return ResolverMainPage.AboutPage()
    elif int == 'Electrical':
        return ResolverMainPage.engineerECE()
    elif int == 'CivilandArch':
        return ResolverMainPage.engineerCAE()
    elif int == 'CivilEngineering':
        return ResolverMainPage.engineerCivil()
    elif int == 'ArchEngineering':
        return ResolverMainPage.engineerArch()
    elif int == 'MechandIndus':
        return ResolverMainPage.engineerMIE()
    elif int == 'MechEngineering':
        return ResolverMainPage.engineerMech()
    elif int == 'IndustEngineering':
        return ResolverMainPage.engineerIndust()
    elif int == 'MechatroEngineering':
        return ResolverMainPage.engineerMecatro()
    elif int == 'Petr&Chem':
        return ResolverMainPage.engineerPCE()
    elif int == 'ChemEngineering':
        return ResolverMainPage.engineerChem()
    elif int == 'PetroEngineering':
        return ResolverMainPage.engineerPetro()
    elif int == 'searchFF':
        return  ResolverMainPage.FFSearch(arg)
    elif int == 'degreePlan':
        return  ResolverMainPage.degreeSearch(arg)
    else:
        return 0
