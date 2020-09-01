def maxRevenu(nbItems, adsList, nbClicksList):
    def specialSort(li):
        positiveList = list(filter(lambda num: num < 0, li))
        negativeList = list(filter(lambda num: num >= 0, li))

        positiveList.sort(reverse=True)
        negativeList.sort()

        return positiveList + negativeList

    adsList = specialSort(adsList)
    nbClicksList = specialSort(nbClicksList)

    revenu = 0
    for i in range(nbItems):
        revenu += adsList[i] * nbClicksList[i]

    return revenu


n = int(input(""))

a = [int(ai) for ai in input("").split(" ")]
b = [int(bi) for bi in input("").split(" ")]

print(maxRevenu(n, a, b))