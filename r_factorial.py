def r_factorial(num):
    if(num == 1):
        return 1
    else:
        return num * r_factorial(num - 1)

print r_factorial(4)


