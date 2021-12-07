puz = [int(x) for x in open("./puzzles/day7_final").readline().split(",")]
crabs = [{"crabID": crab, "horz": crab} for crab in puz]

# Part 1
def calculateFuelCosts(crabs, pos):
    return sum([abs(crab["horz"] - pos) for crab in crabs])


# part two
def gauss(n, start, end):
    return round((n / 2) * (start + end))


def calculateBurningFuelCosts(crabs, pos):
    return sum(
        [gauss(abs(crab["horz"] - pos), 1, abs(crab["horz"] - pos)) for crab in crabs]
    )


# print results
possiblePos = min(
    [calculateFuelCosts(crabs, pos) for pos in range(min(puz), max(puz) + 1)]
)
print("Part1:", possiblePos)

possiblePos2 = min(
    [calculateBurningFuelCosts(crabs, pos) for pos in range(min(puz), max(puz) + 1)]
)
print("Part2:", possiblePos2)
