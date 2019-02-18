name_list = ["zhangshang", "lisi", "wangwu"]

# 1. 取值和取索引
# list index out of range -列表索引超出范围
print(name_list[0])

# 知道数据的内容，想取索引所在位置
# 使用index方法需要注意，如果传递的数据不再列表中，程序会报错！
print(name_list.index("lisi"))


# 2.修改
name_list[1] = "李四"
# list assignment index out of range
# 列表指定的索引超出范围，程序会报错
#name_list[3] = "王小二"


# 3.增加
name_list.append("wengshijie")
# inset方法可以再列表的末尾追加数据
name_list.insert(1, "123")
# extend 方法可以列表的内容全部追加别的列表中
temp_list = ["孙悟空", "猪二哥", "沙师弟"]
name_list.extend(temp_list)


# 4.删除
# remove 方法可以从列表中删除数据指定数据
name_list.remove("猪二哥")

# pop 方法默认可以把最后一个列表中数据删除
name_list.pop()
# pop 方法可以指定删除元素的索引
name_list.pop(3)
# clear 可以清空列表
name_list.clear()

print(name_list)