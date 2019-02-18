# 0-100的偶素求和
# 定义一个变量
even = 0
# 定义一个循环次数
i = 0

while i <= 100:
    if i % 2 == 0:

        even += i
        print(i)

    i += 1
print("0-100的偶素求和= %d" % even)