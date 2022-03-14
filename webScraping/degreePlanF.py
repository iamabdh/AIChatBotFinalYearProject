# add directories for calling submodule
import os, sys
currentDir = os.path.dirname(os.path.realpath(__file__))
parrentDir = os.path.dirname(currentDir)
sys.path.append(parrentDir)


from bs4 import BeautifulSoup
from urllib.request import urlopen
import unicodedata
from datetime import date


def degreePlan(department, year) -> dict:
    """
    :param year:
    :param department: which dept currently user looking for in particular
    :return: msg
    """
    url = f'https://www.squ.edu.om/engineering/Academic/Undergraduate-Programs/{department}'
    mainUrl = 'https://www.squ.edu.om'
    degreePage = urlopen(url)
    html = degreePage.read().decode('utf-8')
    degree_html = BeautifulSoup(html, "html.parser").find_all('div', {'class': 'resp_margin'})[2].find_all('a')
    degreeLinks = []
    for link in degree_html:
        degreeLinks.append(mainUrl + link.get('href'))

    # since only latest available degree plan previous year
    previousYear = date.today().year - 1
    yearDisplacement = previousYear - year

    if yearDisplacement >= (len(degreeLinks) - 1) | (yearDisplacement < len(degreeLinks)):
        return {
            'flag': 27,
            'content': 'Unfortunately, degree plan not available'
        }
    else:
        return {
            'flag': 17,
            'content': degreeLinks[yearDisplacement]
        }