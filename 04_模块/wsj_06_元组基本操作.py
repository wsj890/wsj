info_tuple = ("zhangshan", 18, 1.75)

# 1.取值和取索引
print(info_tuple[0])
# 已经知道数据的内容，希望知道数据在元组的索引
print(info_tuple.index("zhangshan"))


# 2.统计计算
print(info_tuple.count("zhangshan"))

# 统计元组中包含元素的个数
print(len(info_tuple))