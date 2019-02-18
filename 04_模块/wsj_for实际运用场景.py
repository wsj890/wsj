students = [
    {"name": "阿土"},
    {"name": "小美"}
]

# 在学员列表中搜索指定的姓名
find_name = "阿土1"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:

        print("找到了 %s" % find_name)
        # 如果已经找到，应该直接退出循环，而不遍历后续的元素
        break
else:
    # 如果希望在搜索列表是，所有的字典检查之后，都灭有发现搜索目标
    # 还希望找到一个统一的提示
    print("抱歉没有找到 %s" % find_name)
print("循环结束")
