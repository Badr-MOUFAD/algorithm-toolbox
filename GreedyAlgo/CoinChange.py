DENOMINATIONS = [10, 5, 1]


def change(m):
    if m <= 0:
        return 0

    for denomination in DENOMINATIONS:
        difference = m - denomination

        if difference >= 0:
            return 1 + change(difference)

    return


x = int(input(""))
print(change(x))
