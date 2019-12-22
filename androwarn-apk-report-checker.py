import os
import re
from shutil import copyfile
from bs4 import BeautifulSoup
from bs4 import SoupStrainer


def Diff(li1, li2):
    return list(set(li1) - set(li2))


only_body = SoupStrainer('body')
os.chdir('F:/apks')

resultList = []
apkList = []
errorList = []
count = 0

for subdir, dir, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".html"):
            try:
                report = BeautifulSoup(open(file), features="html.parser", parse_only=only_body)
                resultListRaw = report.find_all('div', attrs={"id": "file-name"})
                resultList = resultList + re.findall("<h3>(.*?)<*/*h3>", str(resultListRaw))
            except:
                errorList.append(file)
                print("Error could not open " + file)
        if file.endswith(".apk"):
            apkList.append(file)
            print("Apk file " + file)
        count = count + 1
        print("File:" + str(count))

missingReports = Diff(apkList, resultList)

for item in errorList:
    try:
        copyfile(os.getcwd() + '/' + item, 'F:/Test/' + '/' + item)
    except:
        print(item)

for item in missingReports:
    try:
        copyfile(os.getcwd() + '/' + item, 'F:/Test/' + '/' + item)
    except:
        print(item)
