# 사용하는 크롬의 버전에따라 크롬 드라이버 최신화 및 버전 일치 필요함
# pip install selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from openpyxl import *
from bs4 import BeautifulSoup
import requests
import urllib

link = "https://news.naver.com/breakingnews/section/105/229?date="
date = "20250417"

main_link = link + date
Main_link = pd.DataFrame({"number": [], "title": [], "link": []})

service = Service("etc/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(main_link)
time.sleep(3)

more_button = driver.find_element(
    By.CLASS_NAME, "section_more_inner._CONTENT_LIST_LOAD_MORE_BUTTON"
)

while True:
    try:
        more_button.click()
        time.sleep(3)
    except:
        break

articles = driver.find_elements(By.CLASS_NAME, "sa_text_title._NLOG_IMPRESSION")
for i in range(len(articles)):
    title = articles[i].text.strip()
    link = articles[i].get_attribute("href")
    li = [i + 1, title, link]
    Main_link.loc[i] = li


excel_name = "etc/news_" + date + ".xlsx"
with pd.ExcelWriter(excel_name) as writer:
    Main_link.to_excel(writer, sheet_name="링크", index=False)

# ==================================================================
# 개별 기사 크롤링하기

link = pd.read_excel("etc/news_20250417.xlsx")
excel_name = "etc/news_detail_20250417.xlsx"
Main_link = list(link["link"])
Information = pd.DataFrame({"number": [], "title": [], "information": [], "link": []})
Information["number"] = link["number"]
Information["title"] = link["title"]
Information["link"] = link["link"]
information = []

# 기사의 본문을 크롤링하는 과정을 전체 링크에서 진행해야 한다.
for main_link in Main_link:
    try:
        response = requests.get(main_link, headers={"User-Agent": "Moailla/5.0"})
        if response.status_code == 200:
            html = response.content
            soup = BeautifulSoup(html, "html.parser")
            info = soup.find("div", {"id": "newsct_article"}).text.strip()
            info = info.replace("\n", "")
            information.append(info)
    # IT/과학 카테고리에서 오류가 발생한다는 의미는 e스포츠 카테고리 기사라는 의미이다.
    except:
        try:
            response = requests.get(main_link, headers={"User-Agent": "Moailla/5.0"})
            if response.status_code == 200:
                html = response.content
                soup = BeautifulSoup(html, "html.parser")
                info = soup.find("div", {"id": "newsEndContents"}).text.strip()
                info = info.replace("\n", "")
                end = info.index("기사제공")
                info = info[:end]
                information.append(info)
        # e스포츠 카테고리 기사에서도 오류가 발생한다는 의미는 수집할 필요가 없는 기사라는 의미이다.
        except Exception as e:
            info = ""
            information.append(info)

Information["information"] = information

with pd.ExcelWriter(excel_name) as writer:
    Information.to_excel(writer, sheet_name="결과값", index=False)
