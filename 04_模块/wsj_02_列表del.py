name_list =["张三", "李四", "王五"]

# （知道）使用 del关键字删除列表元素
#  提示：在日常开发中，要从列表删除数据，建议使用列表提供的方法
# 注意 ： 如果使用del关键字 将变量从内存删除
# 后续的代码就不能使用这个变量
del name_list[1]

print(name_list)