import time
from typing import NoReturn

from graia.application import MessageChain, Group, Member
from pydantic.main import BaseModel

class ChatRecord(BaseModel):
    """
    一个用于存储完整的聊天记录的类
    """
    time: float = time.time()
    messagechain: MessageChain
    group: Group
    member: Member

    def __init__(self, messagechain: MessageChain, group: Group, member: Member) -> NoReturn:
        super().__init__(messagechain=messagechain, group=group, member=member)
