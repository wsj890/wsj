# 使用 多个键值对，存储 描述一个物体 的相关信息 ---秒速更加复杂的数据信息
# 将 多个字典 放在 一个列表中，再进行循环遍历

card_list = [
    {"name": "小明",
     "qq": 123456,
     "tel": "110"},
    {"name": "小王",
     "qq": 54321,
     "tel": "119"}
]

for card_info in card_list:
    print(card_info)