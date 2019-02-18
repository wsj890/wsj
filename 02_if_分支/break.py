for element in "Python":
    if  element=='y':
        break
        print (element)
    else:
        print(element)
print ('----'*15)
#break:终止最小的循环层
for i in range(3):
    for element in "Python":
        if  element=='y':
            break
        else:
            print (element)
    print ('****'*15)