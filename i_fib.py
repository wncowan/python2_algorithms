def i_fib(num):

    fibs = [0,1]

    for i in range(0,num):
        fibs.append(fibs[0] + fibs[1])
        fibs.pop(0)

    return fibs[0]

print i_fib(7)

def r_fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return r_fib(num-2) + r_fib(num -1)

print r_fib(7)