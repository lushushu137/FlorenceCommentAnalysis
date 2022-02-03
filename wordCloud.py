# encoding:utf-8 
import wordcloud
import jieba
import jieba.analyse
import pandas as pd
import numpy as np
import collections

jieba.enable_paddle()

w = wordcloud.WordCloud(
    width=1440,
    height=810, 
    font_path="PingFang.ttc",
    background_color = "white",
    collocations=False,
    scale = 2
    )

mystopWords = ["Florence", "游戏", "UU", "点赞", "狗哥", "will", "。", "", "a", "14", "一款", "他人", "Steam", "于是","会", "可以", "没有", "他人", "我花", "然后", "而是","steam","有些", "大过", "中", "里"]
with open("stopwords.txt", "r", encoding='utf-8') as f:
    stopWords = f.read().split("\n")
stopWords = mystopWords + stopWords
with open("onlyComment.txt", "r", encoding='utf-8') as f:
    data = f.read()
    output = jieba.cut(data, use_paddle=True)

    finalRes = ""
    for t in output:
        if t in stopWords:
            continue
        finalRes += (t + " ")
    # w.generate(finalRes)
    # w.to_file('cloud.png')

wordlist = finalRes.split(" ")
counter=collections.Counter(wordlist)
counter = [(x, counter[x]) for x in counter]
counter.sort(key=lambda x:-x[1])
csv = pd.DataFrame(data=dict(word=[x[0] for x in counter], freq=[x[1] for x in counter]))
csv.to_csv("tmp.csv")