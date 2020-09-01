
class Table:
    def __init__(self, s, prevTable=None):
        self.table = []
        self.s = s
        self.prevTable = prevTable

        if self.prevTable is None:
            for i in range(s + 1):
                self.table.append([])

                for j in range(s + 1):
                    if i == 0 and j == 0:
                        self.table[i].append(True)
                        continue

                    self.table[i].append(False)
        return

    def getElement(self, a, b):
        if a < 0 or b < 0:
            return False

        return self.table[a][b]

    def fillTable(self, souvenir):
        for i in range(self.s + 1):
            self.table.append([])
            for j in range(self.s + 1):
                prevTable = self.prevTable.getElement
                self.table[i].append(prevTable(i - souvenir, j) or prevTable(i, j - souvenir) or prevTable(i, j))
        return

    def isPartitionable(self):
        return int(self.table[-1][-1])


def partitioningSouvenirs(souvenirs):
    s = sum(souvenirs) / 3

    if s - int(s) != 0:
        return 0

    s = int(s)

    stages = [Table(s)]

    for i in range(len(souvenirs)):
        nextTable = Table(s, prevTable=stages[i])
        nextTable.fillTable(souvenirs[i])

        stages.append(nextTable)

    return stages[-1].isPartitionable()


n = int(input(""))
souvenirs = [int(c) for c in input("").split(" ")]

print(partitioningSouvenirs(souvenirs))