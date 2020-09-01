import random as rd


def findMajorityElement(arr, n):
    if n == 1:
        return 1

    sortedArr = mergeSort(arr, 0, n)

    count = 1
    for i in range(n - 1):
        if sortedArr[i] == sortedArr[i + 1]:
            count += 1
        else:
            count = 0

        if count > n / 2:
            return 1

    return 0


def mergeSort(arr, low, heigh):
    if heigh - low == 1:
        return [arr[low]]

    if heigh - low == 2:
        a = arr[low]
        b = arr[low + 1]

        if a < b:
            return [a, b]
        else:
            return [b, a]

    middle = int((low + heigh) / 2) + 1
    arr1 = mergeSort(arr, low, middle)
    arr2 = mergeSort(arr, middle, heigh)

    return merge(arr1, arr2, middle - low, heigh - middle)


def merge(arr1, arr2, n1, n2):  # assuming that arr2 and arr2 are sorted
    pointer1 = 0
    pointer2 = 0

    n = n1 + n2
    result = []

    while pointer1 + pointer2 < n:
        if arr1[pointer1] < arr2[pointer2]:
            result.append(arr1[pointer1])
            pointer1 += 1
        else:
            result.append(arr2[pointer2])
            pointer2 += 1

        if pointer1 == n1:
            result += arr2[pointer2:]
            break
        if pointer2 == n2:
            result += arr1[pointer1:]
            break

    return result


# def findMajorityNaive(arr, n):
#     for element in arr:
#         count = 0
#
#         for otherElement in arr:
#             if element == otherElement:
#                 count += 1
#
#         if count > n / 2:
#             return 1
#
#     return 0
#
#
# def genRandomList(n):
#     result = []
#
#     for i in range(n):
#         result.append(rd.randint(0, 3))
#
#     return result


# def FindMajorityELement(n, sequence):
#     if n == 1:
#         return 1
#
#     arrNumbers = sequence
#     arrNumbers.sort()
#
#     count = 1
#     currentElement = arrNumbers[0]
#     for i in range(1, n):
#         if arrNumbers[i] == currentElement:
#             count += 1
#         elif count > n / 2:
#             return 1
#         else:
#             count = 1
#             currentElement = arrNumbers[i]
#
#     return 0


n = int(input(""))
arr = [int(c) for c in input("").split(" ")]


print(findMajorityElement(arr, n))
