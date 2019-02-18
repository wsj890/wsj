
# 定义一个函数打印 由任意 重复次数的 分割线


def print_line(char, times):

    print(char * times)


# print_line("hi", 30)

def print_lines(char1, times2):
    """打印多行字符串

    :param char1: 分割线使用的分割字符
    :param times2: 分割线重复次数
    """
    row = 0

    while row < 5:
        """调用print_line"""
        print_line(char1, times2)
        row += 1


print_lines("-", 20)

print("5", 4)







