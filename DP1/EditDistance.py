
class TwoDimensionTable:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2
        self.table = []

        # setup table
        for i in range(len(self.string1)):
            self.table.append([])
            for j in range(len(self.string2)):
                self.table[i].append((0, "", ""))

        return

    def getElementAt(self, i, j):
        if i < 0 and j < 0:
            return 0, "", ""

        if i < 0:
            s = self.string2[:j + 1]
            length = len(s)
            return length, "-" * length, s

        if j < 0:
            s = self.string1[:i + 1]
            length = len(s)
            return length, s, "-" * length

        return self.table[i][j]

    def setElement(self, i, j, editDistance, string1, string2):
        self.table[i][j] = (editDistance, string1, string2)
        return


def ComputeEditDsitance(string1, string2):
    table = TwoDimensionTable(string1=string1, string2=string2)

    for i in range(len(string1)):
        for j in range(len(string2)):
            ed1 = table.getElementAt(i - 1, j)[0] + 1
            ed2 = table.getElementAt(i, j - 1)[0] + 1

            ed3 = table.getElementAt(i - 1, j - 1)[0]
            if string1[i] != string2[j]:
                ed3 += 1

            table.setElement(i, j, min(ed1, ed2, ed3), "", "")

    print(table.table[-1][-1][0])
    return


s1 = input("")
s2 = input("")

ComputeEditDsitance(s1, s2)
