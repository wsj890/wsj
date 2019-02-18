# 假设：以下内容时从网上抓取的
# 要求：顺序且居中对齐输出
poem = ["\t\n王之涣",
        "白日依山\t\n尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str in poem:
    # 先用strip方法出去字符串空白字符
    # 再用center方法居中显示文本
    print("|%s|" % poem_str.rjust().center(10))