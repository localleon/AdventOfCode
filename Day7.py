puz = [int(x) for x in open("./puzzles/day7_final").readline().split(",")]
crabs = [{"crabID": crab, "horz": crab} for crab in puz]

# Part 1
def calculateFuelCosts(crabs, pos):
    return sum([abs(crab["horz"] - pos) for crab in crabs])


# part two
def gauss(start, n):
    return round((n / 2) * (start + n))


def calculateBurningFuelCosts(crabs, pos):
    return sum([gauss(1, abs(crab["horz"] - pos)) for crab in crabs])


def getPosWithMinFulCost(fuelCostFunc):
    return min([fuelCostFunc(crabs, pos) for pos in range(min(puz), max(puz) + 1)])


# print results
print("Part1:", getPosWithMinFulCost(calculateFuelCosts))
print("Part2:", getPosWithMinFulCost(calculateBurningFuelCosts))
