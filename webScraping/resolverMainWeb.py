
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
         from webScraping import facultyStaff
         if name is not None:
            listingName = name.split()
            listingName.remove(listingName[0])
            name = ' '.join(listingName)
         return facultyStaff.searchFF(name)
    
    def engineer1():
        from webScraping.scrapingENG2 import Engineer
        return Engineer.electrical()

    def engineer2():
        from webScraping.scrapingENG2 import Engineer
        return Engineer.civilandArch()

    def engineer3():
        from webScraping.scrapingENG2 import Engineer
        return Engineer.MechanicalIndustrial()
    
    def engineer4():
        from webScraping.scrapingENG2 import Engineer
        return Engineer.PetroleumChemical()


    



def resloverIntents(int, arg = None):

    if int == 'AboutSQU':
        return ResolverMainPage.AboutPage()
    elif int == 'Electrical':
        return ResolverMainPage.engineer1()
    elif int == 'CivilandArch':
        return ResolverMainPage.engineer2()
    elif int == 'MechandIndus':
        return ResolverMainPage.engineer3()
    elif int == 'Petr&Chem':
        return ResolverMainPage.engineer4()
    elif int == 'searchFF':
        return  ResolverMainPage.FFSearch(arg)
    else:
        return 0
