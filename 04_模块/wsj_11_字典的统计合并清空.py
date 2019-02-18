xiaoming_dict = {"name": "小明",
                 "age": 15,
                 "gender": True,
                 "height": 1.75,
                 "weight": 50
            }
print(len(xiaoming_dict))

# 2.合并字典
tem_dict = {"xixi": 656}
xiaoming_dict.update(tem_dict)
print(xiaoming_dict)

# 3. 清空字典
xiaoming_dict.clear()
print(xiaoming_dict)