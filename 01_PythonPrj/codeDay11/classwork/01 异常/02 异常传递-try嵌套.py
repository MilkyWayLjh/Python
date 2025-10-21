try:
    try:
        try:
            num = int(input('num:'))
            result = 1 / num
        except ZeroDivisionError as e:
            print(e)
    except NameError as e:
        print(e)
except ValueError as e:
    print(e)

