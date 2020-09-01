
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


def numberOfOccurrence(arrSegments, totalLength, point):
    arrRight = list(arrSegments)
    arrRight.sort(key=lambda x: x[0])
    arrRight = [(i, *arrRight[i]) for i in range(totalLength)]

    arrLeft = list(arrRight)
    arrLeft.sort(key=lambda x: x[2])

    pointerRight = positionElement(arrRight, totalLength, point, key=lambda x: x[1])
    # position pointer right in the max right side
    # for i in range(pointerRight + 1, totalLength):
    #     if arrRight[pointerRight][1] == arrRight[i][1]:
    #         pointerRight += 1
    #     else:
    #         break

    # # to include the last element
    # if pointerRight == totalLength -1:
    #     pointerRight = totalLength

    pointerLeft = positionElement(arrLeft, totalLength, point, key=lambda x: x[2])

    # case of : point out side of the segment
    if pointerLeft == totalLength:
        return 0, pointerRight, pointerLeft, arrRight, arrLeft

    # position pointer left in the max left side
    for i in range(pointerLeft - 1, -1, -1):
        if arrLeft[pointerLeft][2] == arrLeft[i][2]:
            pointerLeft -= 1
        else:
            break

    count = 0
    # for i in range(pointerRight):
    #     for j in range(pointerLeft, totalLength):
    #         if i == arrLeft[j][0]:
    #             count += 1

    for i in range(pointerLeft, totalLength):
        if arrLeft[i][0] <= pointerRight:
            count += 1

    return count, pointerRight, pointerLeft, arrRight, arrLeft


print(numberOfOccurrence([(0, 5), (0, 2), (0, 10), (2, 3), (2, 4)], 5, 1))

