try:
    a = int(input('Enter your number:  '))
    b = 1/a
except Exception as e:
    print(e)
    exit()
finally:
    print("we are done")