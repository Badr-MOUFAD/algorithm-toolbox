def optimazedApproch(n):  # get executed in O(n)
    f0 = 0
    f1 = 1

    if n == 0:
        return f0
    if n == 1:
        return f1

    result = 0

    for i in range(1, n):
        result = (f1 + f0) % 10
        f0 = f1
        f1 = result

    return result


x = int(input(""))

print(optimazedApproch(x))
