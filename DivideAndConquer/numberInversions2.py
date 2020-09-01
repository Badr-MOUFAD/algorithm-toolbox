
def mergeSort(arr, low, heigh):
    if heigh - low == 1:
        return [arr[low]], 0

    if heigh - low == 2:
        a = arr[low]
        b = arr[low + 1]

        if a <= b:
            return [a, b], 0
        else:
            return [b, a], 1

    middle = int((low + heigh) / 2) + 1
    arr1, nbInversions1 = mergeSort(arr, low, middle)
    arr2, nbInversions2 = mergeSort(arr, middle, heigh)

    return merge(arr1, arr2, middle - low, heigh - middle, nbInversions1 + nbInversions2)


def merge(arr1, arr2, n1, n2, nbInversions):  # assuming that arr2 and arr2 are sorted
    pointer1 = 0
    pointer2 = 0

    n = n1 + n2
    result = []

    count = nbInversions
    while pointer1 + pointer2 < n:
        if arr1[pointer1] <= arr2[pointer2]:
            result.append(arr1[pointer1])
            pointer1 += 1
        else:
            result.append(arr2[pointer2])
            pointer2 += 1
            count += n1 - pointer1

        if pointer1 == n1:
            result += arr2[pointer2:]
            break
        if pointer2 == n2:
            result += arr1[pointer1:]
            break

    return result, count


n = int(input(""))
arr = [int(c) for c in input("").split(" ")]

print(mergeSort(arr, 0, n)[1])
