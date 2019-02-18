# 计算0-100的求和
# 定义最终结果变量
result = 0

# 定义一个整数边记录循环次数
i = 0
# 开始循环
while i <= 100:
    print(i)
    # 处理计算器
    result = result + i
    i += 1
print("最终的0-100的求和=%d" % result)


