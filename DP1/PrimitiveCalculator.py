
class Table:
    def __init__(self, infinity=10**6):
        # starting from 0
        self.table = [(infinity, []), (0, [1])]  # number of operations / steps to obtain the number

        self.infinity = infinity
        return

    def __getitem__(self, index):
        if index - int(index) != 0:
            return self.table[0]

        return self.table[int(index)]

    def add(self, nbOpertations, steps):
        tup = (nbOpertations, steps)
        self.table.append(tup)
        return

    def __str__(self):
        steps = ""

        for step in self.table[-1][1]:
            steps += str(step) + " "

        return "{0}\n{1}".format(self[-1][0], steps)


def PrimitiveCalculator(n):
    tableCalculator = Table()

    for i in range(2, n + 1):
        minNbOperation = i
        step = []

        count = 0
        for nbOprations in [tableCalculator[i / 3][0], tableCalculator[i / 2][0], tableCalculator[i - 1][0]]:
            if nbOprations < minNbOperation:
                minNbOperation = nbOprations
                if count == 0:
                    step = tableCalculator[i / 3][1] + [i]
                elif count == 1:
                    step = tableCalculator[i / 2][1] + [i]
                else:
                    step = tableCalculator[i - 1][1] + [i]
            count += 1

        tableCalculator.add(minNbOperation + 1, step)

    print(tableCalculator)
    return


n = int(input(""))
PrimitiveCalculator(n)
