
class KnapsackOfGold:
    def __init__(self, W, arrBars):
        self.totalCapacity = W
        self.arrBars = arrBars

        self.table = []
        self.infinity = -10 ** 6

        for w in range(self.totalCapacity + 1):
            self.table.append([])
            for i in range(len(arrBars)):
                decision1 = self.getElement(w - self.arrBars[i], i - 1)[0] + self.arrBars[i]
                decision2 = self.getElement(w, i - 1)[0]

                if decision1 > decision2:
                    # ith element was used
                    self.table[w].append((decision1, self.getElement(w - self.arrBars[i], i - 1)[1] + [i]))
                else:
                    # ith element was not used
                    self.table[w].append((decision2, self.getElement(w, i - 1)[1]))
        return

    def getElement(self, w, i):
        if w < 0:
            return self.infinity, []

        if i < 0:
            return 0, []

        return self.table[w][i]

    def getTotalValue(self):
        return self.table[-1][-1][0]

    def getUsedItems(self):
        return self.table[-1][-1][1]

    def __str__(self):
        # total value
        # weight of used items expressed as an string a1 a2 a3 ...

        strValues = ""
        for index in self.getUsedItems():
            strValues += str(self.arrBars[index]) + " "

        return "{0}\n" \
               "{1}".format(self.getTotalValue(), strValues)


weight, totalItems = [int(s) for s in input("").split(" ")]
arrBarrs = [int(s) for s in input("").split(" ")]

knapsack = KnapsackOfGold(weight, arrBarrs)
print(knapsack)


