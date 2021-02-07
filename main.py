from graia.application import (GraiaMiraiApplication, Session, MessageChain,
                               Member, Group)
from graia.application.message.elements.internal import Plain, Image, At
from graia.broadcast import Broadcast
from src.chatRecord import ChatRecord
from src.record import Record
from src.wordCloudGenerator import wordCloudGenerator
from src.summaryGraphGenerator import summaryGraphGenerator
import asyncio

loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://127.0.0.1:8080",  # 填入 httpapi 服务运行的地址
        authKey="1234567890",  # 填入 authKey
        account=1743234087,  # 你的机器人的 qq 号
        websocket=True  # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)


@bcc.receiver("GroupMessage")
async def GroupMessageHandler(group: Group, member: Member, msgchain: MessageChain):
    Record.addMessage(ChatRecord(messagechain=msgchain, group=group, member=member))
    if msgchain.has(Plain):
        text = msgchain.get(Plain)[0].text
        if text == '#词云生成':
            await app.sendGroupMessage(group, MessageChain.create(
                [At(member.id),
                 Plain('生成中...')]
            ))
            await app.sendGroupMessage(group, MessageChain.create(
                [At(member.id),
                 Image.fromLocalFile(wordCloudGenerator(Record.getAGroupMessageList(group.id)))]
            ))
        elif text == '#今日消息图表':
            await app.sendGroupMessage(group, MessageChain.create(
                [At(member.id),
                 Plain('生成中...')]
            ))
            await app.sendGroupMessage(group, MessageChain.create(
                [At(member.id),
                 Image.fromLocalFile(summaryGraphGenerator("today", Record.getAGroupMessageList(group.id)))]
            ))
        elif text == '#总消息图表':
            await app.sendGroupMessage(group, MessageChain.create(
                [At(member.id),
                 Plain('生成中...')]
            ))
            await app.sendGroupMessage(group, MessageChain.create(
                [At(member.id),
                 Image.fromLocalFile(summaryGraphGenerator("total", Record.getAGroupMessageList(group.id)))]
            ))

if __name__ == "__main__":
    app.launch_blocking()
