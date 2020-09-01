def maxLoot(arrValWeight, weight):
    def criteria(item):
        return item[0] / item[1]

    sortedItems = arrValWeight
    sortedItems.sort(reverse=True, key=criteria)
    W = weight

    maxValue = 0

    for item in sortedItems:
        if W <= 0:
            break

        if W - item[1] >= 0:
            W -= item[1]
            maxValue += item[0]
            continue

        ratio = W / item[1]
        maxValue += item[0] * ratio

    return maxValue


n, capacity = map(int, input("").split(" "))
arr = []

for i in range(n):
    v, w = map(int, input("").split(" "))
    arr.append((v, w))

print(maxLoot(arr, capacity))
