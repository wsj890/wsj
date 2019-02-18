xiaoming_dict = {"name": "小明",
                 "age": 15,
                 "gender": True,
                 "height": 1.75,
                 "weight": 50}
# 迭代遍历字典
# 变量 d 是每一次循环中个，获取键值对的key
for d in xiaoming_dict:
    print("%s - %s" % (d, xiaoming_dict[d]))
