def collectSignature(n, arrSegements):
    arrSegements = arrSegements
    arrSegements.sort(key=lambda segment: segment[0])

    pointer = 0
    i = 0
    listDistinctSegement = []

    while i != n - 1:
        segment = list(arrSegements[pointer])
        for i in range(pointer + 1, n):
            if segment[1] < arrSegements[i][0]:
                listDistinctSegement.append(segment)
                pointer = i
                break
            else:
                segment[0] = arrSegements[i][0]

            if i == n - 1:
                segment[1] = min(segment[1], arrSegements[i][1])
                listDistinctSegement.append(segment)
                return [seg[1] for seg in listDistinctSegement]

    return [seg[1] for seg in listDistinctSegement]


n = int(input(""))
listSegment = []

for i in range(n):
    listSegment.append([int(nb) for nb in input("").split(" ")])


listPoints = collectSignature(n, listSegment)

print(len(listPoints))

answer = ""
for point in listPoints:
    answer += str(point) + " "

print(answer)
