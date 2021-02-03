from typing import List, Literal, Set
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib

from src.chatRecord import ChatRecord
from src.record import Record

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False


# noinspection PyTypeChecker
def messageTimesSort(msglist: List[ChatRecord]) -> List[list]:
    sent_msg_member = []
    for i in msglist:
        if not i.member in sent_msg_member:
            sent_msg_member.append(i.member)
    sort_list = []
    for i in sent_msg_member:
        sort_list.append({'name': i.name, 'times': len(Record.getAMemberMessageList(msglist, i.id))})

    def takeTimes(elem: dict) -> int:
        return elem.get('times')

    sort_list.sort(key=lambda v:v.get('times'), reverse=True)
    name_list = []
    times_list = []
    for i in sort_list:
        name_list.append(i.get('name'))
        times_list.append(i.get('times'))
    return [name_list, times_list]


def summaryGraphGenerator(mode: Literal["total", "today"], msglist: List[ChatRecord]) -> str:
    if mode == "today":
        msglist = Record.getADayMessageList(msglist, datetime.now())
    sorted_list = messageTimesSort(msglist)
    limit_name_list = []
    limit_times_list = []
    limit = 10
    if len(sorted_list[0]) < 10:
        limit = int(len(sorted_list) / 2)
    for i in range(limit):
        limit_name_list.append(sorted_list[0][i])
        limit_times_list.append(sorted_list[1][i])
    plt.figure(figsize=(7.2, 4.8))
    plt.barh(range(len(limit_times_list)), limit_times_list, tick_label=limit_name_list)
    plt.tight_layout()
    plt.savefig("summaryGraphCache.png")
    return "summaryGraphCache.png"
