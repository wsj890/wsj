# 格式字符串后面的'()' 本质上就是元组
print("%s 年龄是 %d 身高 %2.f" % ("小明", 18, 1.75))


info_tuple = ("小明", 18, 2.85)
print("%s 年龄是 %d 身高 %2.f" % info_tuple)

info_str = "%s 年龄是 %d 身高 %2.f" % info_tuple
print(info_str)
