from pandas import *

with open("./puzzles/day4_final") as aocinput:
    numbers = aocinput.readline()
    boards = [
        DataFrame([[*map(int, r.split())] for r in b.split("\n")])
        for b in aocinput.read().strip().split("\n\n")
    ]

won = set()
for num in map(int, numbers.split(",")):
    for b in set(range(len(boards))) - won:
        boards[b][boards[b] == num] = -1
        if any(v == -5 for a in (0, 1) for v in boards[b].sum(axis=a)):
            won.add(b)
            if len(won) == 1 or len(won) == len(boards):
                boards[b][boards[b] == -1] = 0
                print("winner", boards[b].values.sum() * num)
