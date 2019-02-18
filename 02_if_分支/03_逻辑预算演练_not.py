# 定义一个布尔类型变量 is_employee,编写代码判断是否本公司员工
is_employee = False

# 如果是本公司员工
# 在开发中，通常希望某个条件不满足时，执行一些代码，可以用not
# 另外，如果需要拼接复杂的逻辑计算条件，同样也可能使用到not
if not is_employee:
    print("非本公司员工，请勿入内")
