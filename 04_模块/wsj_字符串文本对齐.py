# 假设：以下内容时从网上抓取的
# 要求：顺序且居中对齐输出
poem = ["王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str in poem:
    print("|%s|" % poem_str.center(20," "))