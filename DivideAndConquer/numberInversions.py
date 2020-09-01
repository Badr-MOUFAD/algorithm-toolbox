
def insertionSort(arr, n):
    sortedArr = arr
    nbInversion = 0

    for i in range(n - 2, -1, -1):
        insertionResult, count = insert(sortedArr, i, n)
        sortedArr = insertionResult
        nbInversion += count

    return sortedArr, nbInversion


def insert(arr, index, n):  # index >= 0 and index < n - 1
    def swap(arr, i, j):
        swapElement = arr[i]
        arr[i] = arr[j]
        arr[j] = swapElement
        return

    count = 0

    for i in range(index, n - 1):
        if arr[i] > arr[i + 1]:
            swap(arr, i, i + 1)
            count += 1
        else:
            break

    return arr, count


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


n = int(input(""))
arr = [int(c) for c in input("").split(" ")]

print(insertionSort(arr, n)[1])

