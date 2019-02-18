# 0-100的偶素求和
# 定义一个变量
even = 0
# 定义一个循环几次
i = 0

while i <= 100:
    even += i
    print(i)
    i += 2
print("0-100的偶素求和= %d" %even)
