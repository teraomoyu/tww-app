import requests
from bs4 import BeautifulSoup
import csv
import re
from pdb import set_trace


def get_noun(load_urls):
    html = requests.get(load_urls["noun"])
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
    print(words)
    return words


def get_adjective(load_urls):
    html = requests.get(load_urls["adjective"])
    soup = BeautifulSoup(html.content, "html.parser")
    tables = soup.find_all("table")

    tr_tags = [i.find_all("tr")[1] for i in tables]
    words = [
        re.sub("\xa0|\n|\u2002|＊|（(.*)）|\((.*)\)", "", w)
        for tr_tag in tr_tags
        for td in tr_tag.find_all("td")
        for w in re.split("\n| ", td.get_text())
        if re.search(
            r"[ぁ-んァ-ン一丁-齢龍]", re.sub("\xa0|\n|\u2002|＊|（(.*)）|\((.*)\)", "", w)
        )
    ]
    words = list(set(words))
    set_trace()
    return words


def main():
    load_urls = {
        "noun": "https://jn1et.com/list-noun/",  # 名詞
        "adjective": "https://jn1et.com/list-adjective/",  # 形容詞
        "verb": "https://jn1et.com/list-verb/",  # 動詞
        "adverb": "https://jn1et.com/list-adverbs/",  # 副詞
        "conjunction": "https://jn1et.com/list-conjunction-interrogative/",  # 接続詞・疑問詞
    }
    # nouns = get_noun(load_urls)
    adjectives = get_adjective(load_urls)


if __name__ == "__main__":
    main()
