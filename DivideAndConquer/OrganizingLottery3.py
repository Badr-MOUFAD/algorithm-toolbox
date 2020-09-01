
def positionElement(Arr, totalLength, target, key=None):
    func = lambda x: x
    if key is not None:
        func = key

    arr = list(map(func, Arr))

    return binarySearch(0, totalLength, arr, totalLength, target)


def binarySearch(low, heigh, Arr, totalLength, target):  # assuming that Arr is a sorted array
    # return the index of corresponding target
    # if no element in the array matches the target, return the index
    # where the target should placed
    if low > heigh:
        return low
    if low == totalLength:
        return low

    middle = int((low + heigh) / 2)

    if Arr[middle] == target:
        return middle
    if target < Arr[middle]:
        return binarySearch(low, middle - 1, Arr, totalLength, target)
    if Arr[middle] < target:
        return binarySearch(middle + 1, heigh, Arr, totalLength, target)

    return


def countOccurrence(arrSegmentsLeft, totalLength, target):  # assume that arrSegments is sorted with regard to a
    pointerLeft = positionElement(arrSegmentsLeft, totalLength, target, key=lambda x: x[0])

    compareLimit = pointerLeft + 1 if pointerLeft < totalLength else totalLength

    count = 0
    for i in range(compareLimit):
        if target <= arrSegmentsLeft[i][1]:
            count += 1
    return count


print(countOccurrence([(0, 1), (0, 2), (0, 3)], 3, 2))

# # reading inputs
# s, p = [int(c) for c in input("").split(" ")]
#
# arrSegements = []
# for i in range(s):
#     arrSegements.append([int(c) for c in input("").split(" ")])
#
# arrPoints = [int(c) for c in input("").split(" ")]
# arrSegements.sort(key=lambda x: x[0])
#
# # resolution
# result = ""
#
# for point in arrPoints:
#     result += str(countOccurrence(arrSegements, s, point)) + " "
#
# print(result)
