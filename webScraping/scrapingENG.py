from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.squ.edu.om/engineering/'


page1 = urlopen(url + 'About/College/Welcome-Message') 
html1 = page1.read().decode('utf-8')
aboutENGwelcome_html = BeautifulSoup(html1, "html.parser")
ENGwelcomParagragh_html = aboutENGwelcome_html.find_all('div', {'id': 'dnn_ctr5582_ContentPane'})[0].find_all(['p','li','span']) 
ENGwelcom_text = str()
for textItem in ENGwelcomParagragh_html:
    ENGwelcom_text += textItem.text +'\n'
print(ENGwelcom_text)


page2 = urlopen(url + 'About/College/Vision-and-Mission') 
html2 = page2.read().decode('utf-8')
aboutVM_html = BeautifulSoup(html2, "html.parser")
aboutVMParagragh_html = aboutVM_html.find_all('div', {'id': 'dnn_ContentPane'})[0].find_all(['p','li','span']) 
aboutVM_text = str()
for textItem in aboutVMParagragh_html:
    aboutVM_text += textItem.text +'\n'
print(aboutVM_text)

page3 = urlopen(url + 'About/College/Industrial-Advisory-Board') 
html3 = page3.read().decode('utf-8')
aboutAIB_html = BeautifulSoup(html3, "html.parser")
aboutAIBParagragh_html = aboutAIB_html.find_all('div', {'id': 'dnn_ContentPane'})[0].find_all(['p','li','span']) 
aboutAIB_text = str()
for textItem in aboutAIBParagragh_html:
    aboutAIB_text += textItem.text +'\n'
print(aboutAIB_text)


page4 = urlopen(url + 'About/College/Quality-Assurance-and-Accreditation-Unit') 
html4 = page4.read().decode('utf-8')
aboutQAA_html = BeautifulSoup(html4, "html.parser")
aboutQAAParagragh_html = aboutQAA_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
aboutQAA_text = str()
for textItem in aboutQAAParagragh_html:
    aboutQAA_text += textItem.text +'\n'
print(aboutQAA_text)


page5 = urlopen(url + 'About/College/Safety') 
html5 = page5.read().decode('utf-8')
aboutHSE_html = BeautifulSoup(html5, "html.parser")
aboutHSEParagragh_html = aboutHSE_html.find_all('div', {'id': 'dnn_ContentPane'})[0].find_all(['p','li','span']) 
aboutHSE_text = str()
for textItem in aboutHSEParagragh_html:
    aboutHSE_text += textItem.text +'\n'
print(aboutHSE_text)


page6 = urlopen(url + 'About/Assistant-Deans/Assistant-Dean-for-Postgraduate-and-Research') 
html6 = page6.read().decode('utf-8')
DeansPost_html = BeautifulSoup(html6, "html.parser")
DeansPostParagragh_html = DeansPost_html.find_all('div', {'id': 'dnn_ctr5603_ContentPane'})[0].find_all(['p','li','span','td']) 
DeansPost_text = str()
for textItem in DeansPostParagragh_html:
    DeansPost_text += textItem.text +'\n'
print(DeansPost_text)


page7 = urlopen(url + 'About/Assistant-Deans/Assistant-Dean-for-Undergraduate-Studies') 
html7 = page7.read().decode('utf-8')
DeansUnder_html = BeautifulSoup(html7, "html.parser")
DeansUnderParagragh_html = DeansUnder_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
DeansUnder_text = str()
for textItem in DeansUnderParagragh_html:
    DeansUnder_text += textItem.text +'\n'
print(DeansUnder_text)


page8 = urlopen(url + 'About/Assistant-Deans/Assistant-Dean-for-Training-and-Community-Service') 
html8 = page8.read().decode('utf-8')
x_html = BeautifulSoup(html8, "html.parser")
AssistDeanParagragh_html = x_html.find_all('div', {'id': 'dnn_ContentPane'})[0].find_all(['p','li','span']) 
AssistDean_text = str()
for textItem in AssistDeanParagragh_html:
    AssistDean_text += textItem.text +'\n'
print(AssistDean_text)


page9 = urlopen(url + 'About/Departments/Civil-and-Architectural-Engineering/Welcome-Message') 
html9 = page9.read().decode('utf-8')
CAEwelcom_html = BeautifulSoup(html9, "html.parser")
CAEwelcomParagragh_html = CAEwelcom_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
CAEwelcom_text = str()
for textItem in CAEwelcomParagragh_html:
    CAEwelcom_text += textItem.text +'\n'
print(CAEwelcom_text)


page10 = urlopen(url + 'About/Departments/Civil-and-Architectural-Engineering/Vision-and-Mission') 
html10 = page10.read().decode('utf-8')
CAE_VM_html = BeautifulSoup(html10, "html.parser")
CAE_VMParagragh_html = CAE_VM_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
CAE_VM_text = str()
for textItem in CAE_VMParagragh_html:
    CAE_VM_text += textItem.text +'\n'
print(CAE_VM_text)


page11 = urlopen(url + 'About/Departments/Civil-and-Architectural-Engineering/Quality-Assurance') 
html11 = page11.read().decode('utf-8')
CAE_QA_html = BeautifulSoup(html11, "html.parser")
CAE_QAParagragh_html = CAE_QA_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
CAE_VM_text = str()
for textItem in CAE_QAParagragh_html:
    CAE_VM_text += textItem.text +'\n'
print(CAE_VM_text)


page12 = urlopen(url + 'About/Departments/Civil-and-Architectural-Engineering/Industrial-Advisory-Board') 
html12 = page12.read().decode('utf-8')
CAE_IAB_html = BeautifulSoup(html12, "html.parser")
CAE_IABParagragh_html = CAE_IAB_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
CAE_IAB_text = str()
for textItem in CAE_IABParagragh_html:
    CAE_IAB_text += textItem.text +'\n'
print(CAE_IAB_text)


page13 = urlopen(url + 'About/Departments/Electrical-and-Computer-Engineering/Welcome-Message') 
html13 = page13.read().decode('utf-8')
ECEwelcom_html = BeautifulSoup(html13, "html.parser")
ECEwelcomParagragh_html = ECEwelcom_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
ECEwelcom_text = str()
for textItem in ECEwelcomParagragh_html:
    ECEwelcom_text += textItem.text +'\n'
print(ECEwelcom_text)


page14 = urlopen(url + 'About/Departments/Electrical-and-Computer-Engineering/Vision-and-Mission') 
html14 = page14.read().decode('utf-8')
ECE_VM_html = BeautifulSoup(html14, "html.parser")
ECE_VMParagragh_html = ECE_VM_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
ECE_VM_text = str()
for textItem in ECE_VMParagragh_html:
    ECE_VM_text += textItem.text +'\n'
print(ECE_VM_text)


page15 = urlopen(url + 'About/Departments/Electrical-and-Computer-Engineering/Quality-Assurance') 
html15 = page15.read().decode('utf-8')
ECE_QA_html = BeautifulSoup(html15, "html.parser")
ECE_QAParagragh_html = ECE_QA_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
ECE_QA_text = str()
for textItem in ECE_QAParagragh_html:
    ECE_QA_text += textItem.text +'\n'
print(ECE_QA_text)


page16 = urlopen(url + 'About/Departments/Electrical-and-Computer-Engineering/Industrial-Advisory-Board') 
html16 = page16.read().decode('utf-8')
ECE_IAB_html = BeautifulSoup(html16, "html.parser")
ECE_IABParagragh_html = ECE_IAB_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
ECE_IAB_text = str()
for textItem in ECE_IABParagragh_html:
    ECE_IAB_text += textItem.text +'\n'
print(ECE_IAB_text)


page17 = urlopen(url + 'About/Departments/Mechanical-and-Industrial-Engineering/Welcome-Message') 
html17 = page17.read().decode('utf-8')
MIEwelcom_html = BeautifulSoup(html17, "html.parser")
MIEwelcomParagragh_html = MIEwelcom_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
MIEwelcom_text = str()
for textItem in MIEwelcomParagragh_html:
    MIEwelcom_text += textItem.text +'\n'
print(MIEwelcom_text)


page18 = urlopen(url + 'About/Departments/Mechanical-and-Industrial-Engineering/Vision-and-Mission') 
html18 = page18.read().decode('utf-8')
MIE_VM_html = BeautifulSoup(html18, "html.parser")
MIE_VMParagragh_html = MIE_VM_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
MIE_VM_text = str()
for textItem in MIE_VMParagragh_html:
    MIE_VM_text += textItem.text +'\n'
print(MIE_VM_text)


page19 = urlopen(url + 'About/Departments/Mechanical-and-Industrial-Engineering/Quality-Assurance') 
html19 = page19.read().decode('utf-8')
MIE_QA_html = BeautifulSoup(html19, "html.parser")
MIE_QAParagragh_html = MIE_QA_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
MIE_QA_text = str()
for textItem in MIE_QAParagragh_html:
    MIE_QA_text += textItem.text +'\n'
print(MIE_QA_text)


page20 = urlopen(url + 'About/Departments/Mechanical-and-Industrial-Engineering/Industrial-Advisory-Board') 
html20 = page20.read().decode('utf-8')
MIE_IAB_html = BeautifulSoup(html20, "html.parser")
MIE_IABParagragh_html = MIE_IAB_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
MIE_IAB_text = str()
for textItem in MIE_IABParagragh_html:
    MIE_IAB_text += textItem.text +'\n'
print(MIE_IAB_text)


page21 = urlopen(url + 'About/Departments/Petroleum-and-Chemical-Engineering/Welcome-Message') 
html21 = page21.read().decode('utf-8')
PCEwelcom_html = BeautifulSoup(html21, "html.parser")
PCEwelcomParagragh_html = PCEwelcom_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
PCEwelcom_text = str()
for textItem in PCEwelcomParagragh_html:
    PCEwelcom_text += textItem.text +'\n'
print(PCEwelcom_text)


page22 = urlopen(url + 'About/Departments/Petroleum-and-Chemical-Engineering/Vision-and-Mission') 
html22 = page22.read().decode('utf-8')
PCE_VM_html = BeautifulSoup(html22, "html.parser")
PCE_VMParagragh_html = PCE_VM_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
PCE_VM_text = str()
for textItem in PCE_VMParagragh_html:
    PCE_VM_text += textItem.text +'\n'
print(PCE_VM_text)


page23 = urlopen(url + 'About/Departments/Petroleum-and-Chemical-Engineering/Quality-Assurance') 
html23 = page23.read().decode('utf-8')
PCE_QA_html = BeautifulSoup(html23, "html.parser")
PCE_QAParagragh_html = PCE_QA_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
PCE_QA_text = str()
for textItem in PCE_QAParagragh_html:
    PCE_QA_text += textItem.text +'\n'
print(PCE_QA_text)


page24 = urlopen(url + 'About/Departments/Petroleum-and-Chemical-Engineering/Industrial-Advisory-Board') 
html24 = page24.read().decode('utf-8')
PCE_IAB_html = BeautifulSoup(html24, "html.parser")
PCE_IABParagragh_html = PCE_IAB_html.find_all('div', {'id': 'dnn_TopPane'})[0].find_all(['p','li','span']) 
PCE_IAB_text = str()
for textItem in PCE_IABParagragh_html:
    PCE_IAB_text += textItem.text +'\n'
print(PCE_IAB_text)

