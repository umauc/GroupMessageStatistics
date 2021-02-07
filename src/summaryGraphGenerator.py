from typing import List, Literal, Set
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib


from src.chatRecord import ChatRecord
from src.record import Record

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


def messageTimesSort(memberlist, msglist) -> List[list]:
    sorted_list = []
    for i,j in zip(memberlist[0], memberlist[1]):
        sorted_list.append([j, len(Record.getAMemberMessageList(msglist, i))])
    sorted_list.sort(key=lambda v: v[1], reverse=True)
    return sorted_list


def summaryGraphGenerator(mode: Literal["total", "today"], msglist: List[ChatRecord]) -> str:
    if mode == "today":
        msglist = Record.getADayMessageList(msglist, datetime.now())
    member_id_list = set()
    member_name_list = set()
    for i in msglist:
        member_id_list.add(i.member.id)
        member_name_list.add(i.member.name)
    sorted_list = messageTimesSort([member_id_list,member_name_list], msglist)
    limit_name_list = []
    limit_times_list = []
    if len(sorted_list) < 10:
        limit = len(sorted_list)
    else:
        limit = 10
    for i in range(limit):
        limit_name_list.append(sorted_list[i][0])
        limit_times_list.append(sorted_list[i][1])
    plt.figure(figsize=(7.2, 4.8))
    plt.barh(range(len(limit_times_list)), limit_times_list, tick_label=limit_name_list)
    plt.tight_layout()
    plt.savefig("summaryGraphCache.png")
    return "summaryGraphCache.png"
