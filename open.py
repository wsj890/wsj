while True:
        try:
            x = int(input("Please enter a number: "))
            break
            print('输入的值%s' % x)
        except ValueError:
            print("Oops!  That was no valid number.  Try again   ")