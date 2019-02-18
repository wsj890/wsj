# 定义字符变量 name，输出 我的名字叫  小明，请多多关照
name = "小明"
print("我的名字叫 %s，请多多关照" % name)

# 定义整数变量 student_no,输出 我的学号是 00001
student_no = 10
print("我的学号是 %04d" % student_no)


# 定义小数 price、weight、money，输出苹果单价 9.00元/斤，购买了 5.00斤，需要支付45.00元
price = 9
weight = 5
money = 45
print("苹果的单价 %.02f,购买了 %.03f，需要支付 %0.4f" % (price, weight, money))

# 定义一个小数 scale，输出 数据比例是10.00%
scale = 0.25 * 100
print("数据比例 %.02f%%" % scale)

scale = 0.25
print("数据比例 %.02f%%" % scale * 100)  # 字符串 * 5 相当于乘以 5次

scale = 0.25
print("数据比例 %.02f%%" % (scale * 100))  # 字符串 * 5 用括号括起来 算数用算符
