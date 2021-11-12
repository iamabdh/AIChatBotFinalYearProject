
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
         return facultyStaff.searchFF(name)



def resloverIntents(int, arg = None):
    return {
        'AboutSQU' : ResolverMainPage.AboutPage(),
        'searchFF' : ResolverMainPage.FFSearch(arg),
    }.get(int, 0) # return 0 if the resolver doesnt find match requests

