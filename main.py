import random,json

version_num = "v0.0.1"

# with open('data.json','r',encoding='utf8')as file:
#     所有海螺的话 = json.load(file)
# 一个计划中的外置语料库，目前直接内置在此文件中

所有海螺的话 = ["那很好",
        "棒极了",
        "但愿如此",
        "可以",
        "不可以",
        "你在开玩笑吗",
        "显然一个海螺是不会知道这些的",
        "我是神奇海螺",
        "你会失望的",
        "你会后悔的",
        "你会被拒绝的",
        "这根本不可能",
        "大胆去爱",
        "这将是一种金钱的浪费",
        "不会有结果的",
        "这是一个极其危险的举动",
        "想开一点",
        "没什么过不去的",
        "假",
        "这不是你想的那样",
        "新年快乐",
        "做你自己",
        "坚持你的选择",
        "如你所愿",
        "Oops,海螺刚才走神了；再问一遍试试？",
        "马上",
        "愿你开心",
        "或许这不是真相",
        "Easier said than done",
        "放轻松"
]

random.shuffle(所有海螺的话) # 先打乱一下顺序，虽然本来就是乱的

print("神奇海螺" + version_num + "\n")

input("嗨，这里是神奇海螺。\n迷失的人啊，你有什么问题需要我的帮助吗？\n") # 先问再抽会显得有礼貌一点:)

print(random.choice(所有海螺的话))

input("回车以退出此程序，重新打开以再次咨询神奇的海螺。")