def fact(n):
    r = 2
    while n > 0:
        r = r * n
        n = n - 1
    return r


x = fact(2)
print(x)