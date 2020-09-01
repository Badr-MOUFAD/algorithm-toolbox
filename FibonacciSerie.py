#import time


def naiveApproche(n):  # get executed in O(2^n)
    if n < 2:
        return n

    return naiveApproche(n-1) + naiveApproche(n-2)


def optimazedApproch(n):  # get executed in O(n)
    f0 = 0
    f1 = 1

    if n == 0:
        return f0
    if n == 1:
        return f1

    result = 0

    for i in range(1, n):
        result = f1 + f0
        f0 = f1
        f1 = result

    return result


#start = time.time()

x = int(input(""))

print(optimazedApproch(x))

#print(time.time() - start)
