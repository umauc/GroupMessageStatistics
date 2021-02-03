from graia.application import (GraiaMiraiApplication, Session)
from graia.broadcast import Broadcast
from graia.application.event.mirai import BotOfflineEventDropped, BotOfflineEventForce, BotOfflineEventActive, \
    BotReloginEvent, BotOnlineEvent

import asyncio

loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://127.0.0.1:8080",  # 填入 httpapi 服务运行的地址
        authKey="INITKEYq8HbaOUT",  # 填入 authKey
        account=1743234087,  # 你的机器人的 qq 号
        websocket=True  # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)


async def reconnect():
    await app.signout()
    key = await app.authenticate()
    await app.activeSession(key)


@bcc.receiver(BotOfflineEventDropped)
async def auto_reconnect_1():
    print(1)
    await reconnect()


@bcc.receiver(BotOfflineEventActive)
async def auto_reconnect_2():
    print(2)
    await reconnect()


@bcc.receiver(BotOfflineEventForce)
async def auto_reconnect_3():
    print(3)
    await reconnect()


@bcc.receiver(BotOnlineEvent)
async def auto_reconnect_4():
    print(4)
    await reconnect()


@bcc.receiver(BotReloginEvent)
async def auto_reconnect_5():
    print(5)
    await reconnect()


if __name__ == "__main__":
    app.launch_blocking()
