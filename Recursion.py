def memoize(f):
    c = {}

    def fact(*args):
        if args in c:
            return c[args]
        else:
            c[args] = f(*args)
            return c[args]

    return fact


def factorial(n):
    if ((n == 0) or (n == 1)):
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(int(input())))