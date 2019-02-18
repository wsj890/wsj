
# 在默认情况下，print 函数输出内容之后，会自动在内容末尾增加换行
# print("*", end="")
# print("**")

row = 1

while row <= 9:

    # 每一行要打印的*是和当前列是一样
    # 增加一个小的循环，专门负责当前行中，每一‘列’显示
    # 1.定义一个计数器变量
    col = 1
    # 2.开始循环

    while col <= row:
        # print("%d" % col)
        print("%d * %d = %d" % (row, col, row * col), end=" ")
        col += 1

    print("")
    row += 1