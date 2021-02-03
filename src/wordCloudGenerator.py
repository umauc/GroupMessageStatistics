from sys import path
from typing import List

import jieba
import wordcloud
from graia.application.message.elements.internal import Plain

from src.chatRecord import ChatRecord

from os import path


def wordCloudGenerator(msglist: List[ChatRecord]) -> str:
    font_path = path.abspath(path.dirname(path.dirname('.'))) + '\\data\\SourceHanSans-Normal.ttc'
    text = ''
    for i in msglist:
        if not i.messagechain.has(Plain):
            continue
        wordlist = jieba.lcut(i.messagechain.get(Plain)[0].text)
        for j in wordlist:
            text = text + j + ' '
    w = wordcloud.WordCloud(font_path=font_path)
    w.generate(text)
    w.to_file('wordCloudCache.png')
    return 'wordCloudCache.png'
