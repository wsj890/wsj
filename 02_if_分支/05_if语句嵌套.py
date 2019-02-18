# 定义布尔类型变量 has_ticket 表示是否有火车票
has_ticket = True
# 定义整数变量 knife_length 表示 长度，单位：里面
knife_length = 25
# 首先检查是否有车票，如果有才能进行安检
if has_ticket:
    # 安检是，需要检查刀的长度 是否超过 20cm
    if knife_length >= 20:
        # 如果超过20，提示刀长度过长，输出刀子 是30公分不能上车
        print("输出刀子 是% d公分不能上车" % knife_length)
    # 如果不超过20，安全通过
    else:
        print("可以通过")
# 如果没有车票，不予许进入
else:
    print("不允许进入")
