def carFuelling(totalDistance, distanceAtFullTank, nbStations, stations):
    stations = [0] + stations + [totalDistance]

    pointer = 0
    nbStops = 0

    while pointer <= nbStations:
        if stations[pointer + 1] - stations[pointer] > distanceAtFullTank:
            return -1

        if stations[-1] - stations[pointer] <= distanceAtFullTank:
            break

        distance = 0
        for i in range(pointer, nbStations + 1):
            distance += stations[i + 1] - stations[i]
            if distance > distanceAtFullTank:
                pointer = i
                nbStops += 1
                break

    return nbStops


d = int(input(""))
m = int(input(""))
nbStations = int(input(""))

arrStations = [int(s) for s in input("").split(" ")]

print(carFuelling(d, m, nbStations, arrStations))
