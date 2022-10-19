import requests
from bs4 import BeautifulSoup
import csv
import re
from pdb import set_trace

f = open("words.csv", "w")
writer = csv.writer(f)
load_urls = [
    "https://jn1et.com/list-noun/",
    # "https://jn1et.com/list-adjective/",
    # "https://jn1et.com/list-verb/",
    # "https://jn1et.com/list-adverbs/",
    # "https://jn1et.com/list-conjunction-interrogative/"
]
rows = []
for load_url in load_urls:
    html = requests.get(load_urls[0])
    soup = BeautifulSoup(html.content, "html.parser")
    tables = soup.find_all("table")
   
    tr_tags = [i.find_all("tr") for i in tables]
    words = [
        [
            re.sub("\n|\u2002|＊|［(.*)］", "", w)
            for p_tag in tr.find_all("p")
            for w in re.split("[,（）／]", p_tag.get_text())
            if re.sub("\n|\u2002|＊|［(.*)］", "", w) != "" and w.find("～") == -1
        ]
        if len(tr.find_all("p")) != 0
        else [
            re.sub("\n|\u2002|＊|［(.*)］", "", w)
            for td_tag in tr.find_all("td")
            for w in re.split("[,（）／]", td_tag.get_text())
            if re.sub("\n|\u2002|＊|［(.*)］", "", w) != "" and w.find("～") == -1
        ]
        for tr_tag in tr_tags
        for index, tr in enumerate(tr_tag)
        if index % 2 != 0
    ]
    words = sum(words, [])
    print(len(words))
