str_1 = "0123456789"
# 截取从2-5位置的字符串
print(str_1[2:5])

# 截取2 到末尾的字符串
print(str_1[2:])

# 截取从开始到 5位置的字符串
print(str_1[0:6])

# 截取完整的字符串
print(str_1[0:])
print(str_1[:])

# 从开始位置，每隔一个字符串截取字符串
print(str_1[0:9:2])

# 从索引 1开始，每隔一个取一个
print(str_1[1:9:2])

# 截取从 2 到末尾 -1的字符串
print(str_1[2:-1])

# 截取字符串末尾两个字符串
print(str_1[-2:])

# 字符串的逆序
print(str_1[-1::-1])
print(str_1[::-1])
