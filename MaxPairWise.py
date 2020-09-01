import time
import random

import plotly.graph_objects as go
import plotly.io as pio


pio.templates.default = "plotly_white"


def naiveMaxPairWise(n, listNumber):
    prevMax = 0

    for i in range(n):
        for j in range(n):
            if i != j:
                product = listNumber[i] * listNumber[j]
                if product > prevMax:
                    prevMax = product

    return prevMax


def optimizedMaxPairWise(n, listNumber):
    def findIndex(sequence, length, skipIndex=None):
        index = 0 if skipIndex != 0 else 1
        currentMax = sequence[0]

        for i in range(1, length):
            if i == skipIndex:
                continue

            if currentMax < sequence[i]:
                index = i
                currentMax = sequence[i]

        return index

    index1 = findIndex(listNumber, n)
    index2 = findIndex(listNumber, n, index1)

    return listNumber[index1] * listNumber[index2]


def fasterMaxPairWise(n, listNumber):
    li = listNumber

    def swap(index):
        swapElement = li[index]
        li[index] = li[index + 1]
        li[index + 1] = swapElement
        return

    nextStarting = 0

    for i in range(n - 1):
        if li[i] > li[i+1]:
            swap(i)
            continue

        nextStarting = i

    for i in range(nextStarting, n - 2):
        if li[i] > li[i+1]:
            nextStarting = i

    return li[-1] * li[nextStarting]


def potentialFasterMaxPairWise(n, listNumber):
    pointer1 = 0
    pointer2 = 0

    for i in range(n):
        if listNumber[pointer1] < listNumber[i]:
            swapPointers = pointer1
            pointer1 = i
            pointer2 = swapPointers

    for i in range(pointer1 + 1, n):
        if listNumber[pointer2] < listNumber[i]:
            pointer2 = i

    return listNumber[pointer1] * listNumber[pointer2]


def generateList(size):
    result = []

    for i in range(size):
        result.append(random.randint(0, 100))

    return result


def runTime(func, *args):
    start = time.time()

    func(*args)

    return time.time() - start


lengthList = 1000000
testList = generateList(lengthList)

iteration = list(range(100))
runTimeOpt = []
runTimeFast = []

for i in iteration:
    runTimeOpt.append(runTime(optimizedMaxPairWise, lengthList, testList))
    runTimeFast.append(runTime(potentialFasterMaxPairWise, lengthList, testList))


fig = go.Figure()

fig.add_trace(go.Scatter(x=iteration, y=runTimeOpt,
                    mode='lines+markers',
                    name='optimized algo'))
fig.add_trace(go.Scatter(x=iteration, y=runTimeFast,
                    mode='lines+markers',
                    name='faster algo'))

fig.update_layout(
    title="Algorithm comparaison (data size = 1 000 000)",
    xaxis_title="iteration",
    yaxis_title="run time in s",
    font=dict(
        family="Courier New",
        size=18,
    )
)


fig.show()



