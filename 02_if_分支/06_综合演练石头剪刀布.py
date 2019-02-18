import random
# 从控制台输入要出的--石头(1)/剪刀(2)/布(3)
player = int(input("请要输入的拳 石头(1)/剪刀(2)/布(3)"))
# 电脑 随机 出拳 - -先假设电脑只会石头，完成代码
computer = random.randint(1, 3)
print("玩家输入拳头是 %d - 电脑出的拳是 %d" % (player, computer))
# 判断胜负
# 石头 胜 剪刀
# 剪刀 胜 布
# 布 胜 石头
# if() or () or ()
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("玩家胜利")
# 平局
elif player == computer:
    print("平局")
# 我输了
else:
    print("我输了")
