hello_str = "hello hello"
# 1.统计字符串长度
print(len(hello_str))

# 2.统计某一个小字符串出现的次数
print(hello_str.count("llo"))

# 3.某一个字符出现的位置
print(hello_str.index("e"))

print(hello_str.upper())

# 判断一个字符是否是空白
print(hello_str.isspace())

space_str = "    \t\n\n"
print(space_str.isspace())