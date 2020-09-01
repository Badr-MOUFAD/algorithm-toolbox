
def findOccurrence(arrSegements, point):
    count = 0

    for segment in arrSegements:
        if segment[0] < point < segment[1]:
            count += 1

    return count


# reading inputs
s, p = [int(c) for c in input("").split(" ")]

arrSegement = []
for i in range(s):
    arrSegement.append([int(c) for c in input("").split(" ")])

arrPoints = [int(c) for c in input("").split(" ")]

# resolution
result = ""

for point in arrPoints:
    result += str(findOccurrence(arrSegement, point)) + " "

print(result)

