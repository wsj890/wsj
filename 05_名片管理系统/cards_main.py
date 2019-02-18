# 无限虚幻，由用户主动决定什么时候退出
while True:
    # TODO(小明) 显示功能菜单

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # TODO 1,2,3 针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 如果在开发程序时，不希望立刻编写分支内部代码
        # 可以使用pass 关键字表示一个占位符，能保证程序的代码结果正确
        # 程序运行时，pass关键字不会被执行
        pass
    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break
        # pass
    # 其他内容输入错误，需要提示用户
    else:
        print("你输入的错误，请重新选择")