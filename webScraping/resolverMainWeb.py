

class ResolverMainPage:

    def AboutPage():
        import aboutPage
        return aboutPage.readAboutSQU() 



def resloverIntents(int):
    return {
        'AboutSQU' : ResolverMainPage.AboutPage()

    }.get(int, 0) # return 0 if the resolver doesnt find match requests

print(resloverIntents("sss"))
