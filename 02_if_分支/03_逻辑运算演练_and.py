# 练习1:定义一个整数变量 age，编写代码判断年龄是否正确
age = int(input("输入一个年龄"))

# 要求人的年龄在 0-120 之间
if age >= 0 and age <= 120:
    print("你的年龄是符合要求")
else:
    print("年龄不正确")