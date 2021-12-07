puz = [line.strip().split(",") for line in open("./puzzles/day5_final")]
coords = []

# parse input
for i in puz:
    x1 = i[0]
    y1 = i[1].split(" ")[0]
    x2 = i[1].split(" ")[2]
    y2 = i[2]
    coords.append([(int(x1), int(y1)), (int(x2), int(y2))])

lines = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], coords))


x1_max = max(lines, key=lambda x: x[0][0])[0][0]
x2_max = max(lines, key=lambda x: x[0][1])[0][1]
y1_max = max(lines, key=lambda x: x[1][0])[1][0]
y2_max = max(lines, key=lambda x: x[1][1])[1][1]

diagram = [["."] * (max(x1_max, x2_max) + 1) for i in range((max(y1_max, y2_max) + 1))]


def incrementDiag(x, y):
    if diagram[y][x] != ".":
        diagram[y][x] = int(diagram[y][x]) + 1
    else:
        diagram[y][x] = 1


for cord in lines:
    # print x coordinates
    x_0, x_1 = min(cord[0][0], cord[1][0]), max(cord[0][0], cord[1][0])
    y_0, y_1 = min(cord[0][1], cord[1][1]), max(cord[0][1], cord[1][1])
    for x in range(x_0, x_1 + 1):
        # print y coordinates
        for y in range(y_0, y_1 + 1):
            incrementDiag(x, y)

flatten = [item for sublist in diagram for item in sublist]

part1_res = len(list(filter(lambda x: x not in [".", 1], flatten)))
print(part1_res)
