name_list =["张三", "李四", "王五"]

# 使用迭代遍历列表
"""
顺序的从列表中依次获取数据，每次循环过程中，数据
都会保存my_name这个变量中，在循环体内部可以访问到当前这次获取到的
数据

for my_name in   列表变量：
    print（------）

"""

for my_name in name_list:
    print("我的名字是 %s"% my_name)
