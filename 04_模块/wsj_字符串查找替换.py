str_num = "hello word"

# 1.字符串是否以指定字符串开头
print(str_num.startswith("Hel"))

# 2.判断是否以指定字符串结束
print(str_num.endswith("d"))

# 3.查找指定字符串
# index 同样可以查找指定字符串在大写字符串中索引
# index如果指定字符不存在，会报错
# find 如果指定字符串不存在，会返回 -1
print(str_num.find("llo"))
print(str_num.find("abc"))


# 4.替换字符串
# replace方法执行完成之后，会返回一个新的字符串
# 注意：不会修改原有字符串的内容
print(str_num.replace("o", "kkk"))
print(str_num)


