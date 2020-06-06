
# -*- coding:utf-8 -*-
import requests
import sys
import re
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np
from lxml import etree
 
headers = {
       'Referer'  :'http://music.163.com',
       'Host'     :'music.163.com',
       'Accept'   :'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
       'User-Agent':'Chrome/10'
    }
page_url = 'http://music.163.com/api/playlist/detail?id=753776811'
# ªÒ»°Õ¯“≥HTML
res = requests.request('GET', page_url, headers=headers)
print(len(res.json()['result']['tracks']))
song_ids = []
song_names = []

for i in range(len(res.json()['result']['tracks'])):
    ids = res.json()['result']['tracks'][i]['id']
    names = res.json()['result']['tracks'][i]['name']
    song_ids.append(ids)
    song_names.append(names)
    print(names, '', ids)