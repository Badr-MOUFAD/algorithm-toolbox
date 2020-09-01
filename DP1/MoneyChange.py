
class Table:
    def __init__(self, infinity=10**6):
        self.table = [0]
        self.infinity = infinity
        return

    def __getitem__(self, index):
        if index < 0:
            return self.infinity

        return self.table[index]

    def add(self, value):
        self.table.append(value)
        return


def ChangeMoney(money, arrDenominations):
    tableChange = Table()

    for i in range(1, money + 1):
        actions = []

        for denomination in arrDenominations:
            actions.append(tableChange[i - denomination] + 1)

        tableChange.add(min(actions))

    return tableChange.table[-1]


money = int(input(""))

print(ChangeMoney(money, [1, 3, 4]))
