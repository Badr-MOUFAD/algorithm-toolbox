# low and heigh are within the range of Arr length


def binarySearch(low, heigh, Arr, totalLength, target):
    if low > heigh:
        return -1
    if low == totalLength:
        return -1

    middle = int((low + heigh) / 2)

    if Arr[middle] == target:
        return middle
    if target < Arr[middle]:
        return binarySearch(low, middle - 1, Arr, totalLength, target)
    if Arr[middle] < target:
        return binarySearch(middle + 1, heigh, Arr, totalLength, target)

    return


[n, *a] = list(map(int, input("").split(" ")))
[k, *b] = list(map(int, input("").split(" ")))

result = ""

for target in b:
    result += str(binarySearch(low=0, heigh=n, Arr=a, totalLength=n, target=target)) + " "

print(result)