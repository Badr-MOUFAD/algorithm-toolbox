#import time


def naiveGCD(a, b):
    n = min(a, b)

    for i in range(n, 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return


def optimizedGCD(a, b):
    m = max(abs(a), abs(b))
    n = min(abs(a), abs(b))

    if n == 0:
        return m

    return optimizedGCD(n, m - int(m/n) * n)


x, y = map(int, input("").split(" "))

#start = time.time()

print(int(x*y / optimizedGCD(x, y)))

#print(time.time() - start)
