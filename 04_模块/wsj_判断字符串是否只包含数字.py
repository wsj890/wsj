# 判断字符串是否只包含数字

# 1.都不能判断小数
# num_str = "1.2"

# 2.unicode 字符串
# num_str = "\u00b2"

# 3.中文数字
num_str = "一千零一"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())