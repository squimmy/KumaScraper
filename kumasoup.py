import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

chapterNum = 1

with open("kumacount.txt", "a", encoding="utf-8") as countFile:
    for pageNum in range(5, 674):
        URL = "https://ncode.syosetu.com/n4185ci/" + str(pageNum)
        page = requests.get(URL, headers=headers).text
        soup = BeautifulSoup(page, "lxml")

        for kuma in soup.find_all('div', id="novel_honbun"):
            charCount = len(kuma.text)
            countFile.write(f"{chapterNum}, {charCount}\n")
            print(f"{chapterNum}, {charCount}, {URL}")
            
            chapterNum += 1
