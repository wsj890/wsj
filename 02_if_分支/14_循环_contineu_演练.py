i = 0

while i <= 10:
    # continue 当i == 3，不再执行后面重复条件
    if i == 3:
        # 注意：在循环中，如果使用 continue 这个关键字
        # 使用关键字之前，需要确认循环技术是否修改
        # 否者可能死循环
       # i += 1
        continue

    print(i)

    i += 1
print("over")