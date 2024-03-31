

def babySqrt(n: int):
    x = n
    acc = 0.000000001
    y = 1
    while (x-y) > acc:
        x = (x+y)/2
        y = n/x

    return x



print(babySqrt(2))