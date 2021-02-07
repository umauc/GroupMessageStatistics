import datetime as datetime
import pickle
from os import path
import os
from typing import List, NoReturn

from graia.application import Source

from src.chatRecord import ChatRecord


class Record(object):
    cachedMessage = []
    datPath = path.abspath(path.dirname(path.dirname('.'))) + '\\data\\chatRecord.dat'
    if os.path.getsize(datPath) > 0:
        cachedMessage = pickle.load(open(datPath, 'rb'))
        print('加载成功！')

    @classmethod
    def addMessage(cls, chatrecord: ChatRecord) -> NoReturn:
        cls.cachedMessage.append(chatrecord)
        pickle.dump(cls.cachedMessage, open(cls.datPath, 'wb'))

    @staticmethod
    def getAMemberMessageList(msglist: List[ChatRecord], qid: int) -> list:
        for i in msglist:
            if i.member.id != qid:
                msglist.remove(i)
        return msglist

    @classmethod
    def getAGroupMessageList(cls, groupid: int) -> list:
        msglist = []
        for i in cls.cachedMessage:
            if i.group.id == groupid:
                msglist.append(i)
        return msglist

    @staticmethod
    def getADayMessageList(msglist: List[ChatRecord], date: datetime):
        for i in msglist:
            if i.messagechain.get(Source)[0].time != date:
                msglist.remove(i)
        return msglist
