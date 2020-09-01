
def quickSort(arr):
    length = arr.__len__()

    if length <= 1:
        return arr

    pivot = arr[0]
    leftArr, middleArr, rightArr = [], [pivot], []

    for i in range(1, length):
        if pivot == arr[i]:
            middleArr.append(arr[i])
        elif pivot < arr[i]:
            rightArr.append(arr[i])
        elif arr[i] < pivot:
            leftArr.append(arr[i])

    return quickSort(leftArr) + middleArr + quickSort(rightArr)


n = int(input(""))
arr = [int(c) for c in input('').split(" ")]

arr = quickSort(arr)
result = ""

for nb in arr:
    result += str(nb) + " "

print(result)
