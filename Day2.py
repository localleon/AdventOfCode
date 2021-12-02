puz = [line.strip("\n").split(" ") for line in open("./puzzles/day2_final")]
# its 23:00 after training , please forgive my dirty code

# part 1

horz = 0
depth = 0
aim = 0

for move in puz:
    x = int(move[1])

    if move[0] == "forward":
        horz += x
    elif move[0] == "down":
        depth += x
    elif move[0] == "up":
        depth -= x

print(f'horz {horz}, depth {depth}')
print(horz*depth)

# part 2

horz = 0
depth = 0
aim = 0

for move in puz:
    x = int(move[1])

    if move[0] == "forward":
        horz += x
        depth += aim * x
    elif move[0] == "down":
        aim += x
    elif move[0] == "up":
        aim -= x
print(f'horz {horz}, depth {depth}')
print(horz*depth)
