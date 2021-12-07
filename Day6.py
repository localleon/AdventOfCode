# new laternfisch every 7 days
# first cycle +2 days for start


puz = [int(timer) for timer in open("./puzzles/day6_final").readline().split(",")]


def reduceAll(puz):
    return list(map(lambda x: x - 1, puz))


def simulateFishDay(fishes):
    newFishCounter = 0
    for i, fish in enumerate(fishes):
        fishes[i] -= 1
        if fishes[i] == -1:
            newFishCounter += 1
            fishes[i] = 6
    fishes.extend([8] * newFishCounter)
    return fishes


def simulateOverDays(fishes, days):
    evolution = []
    for day in range(days):
        evolution = simulateFishDay(fishes)
        # print("Day:", day + 1, ",".join([str(x) for x in evolution]))
    return evolution


print("Initial State: ", puz)
print("Part 1", len(simulateOverDays(puz.copy(), 8)))
print("Part 2", len(simulateOverDays(puz.copy(), 256)))
