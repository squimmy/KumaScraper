from typing import Text
import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

pageNum = 5
chapterNum = 1
URL = "https://ncode.syosetu.com/n4185ci/" + str(pageNum)

while pageNum < 674:
    page = requests.get(URL, headers=headers).text
    soup = BeautifulSoup(page, "lxml")
    file = open("kumaclean.txt", "w", encoding="utf=8")

    for kuma in soup.find_all('div', id="novel_honbun"):
        
        contents = kuma.text
        file.write(contents)
        
        count = open("kumaclean.txt", "r", encoding="utf-8")
        countFile = open("kumacount.txt", "a", encoding="utf-8")
        data = count.read()
        charCount = len(data)
        countFile.write(str(chapterNum) + ', ' + str(charCount) + '\n')
        print(str(chapterNum) + ', ' + str(charCount) + ", " + URL)
        
        pageNum += 1
        chapterNum += 1
            
    URL = "https://ncode.syosetu.com/n4185ci/" + str(pageNum)