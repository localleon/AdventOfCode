puz = [list(line.strip("\n")) for line in open("./puzzles/day3_final")]

gamma = ""
epsilon = ""

for i in range(len(puz[0])):
    if [mes[i] for mes in puz].count("0") > [mes[i] for mes in puz].count("1"):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print("Part1: ", int(gamma, 2)*int(epsilon, 2))

# ============ part 2 ====================

def readings(puz, compareF):
    for i in range(len(puz[0])):
        zero = [mes[i] for mes in puz].count("0")
        one = [mes[i] for mes in puz].count("1")
        if compareF(one, zero):
            # oxygen generator
            puz = [mes for mes in puz if mes[i] == ("1")]
        else:
            puz = [mes for mes in puz if mes[i] == ("0")]
        if len(puz) == 1:
            return int("".join(puz[0]), 2)


oxygen = readings(puz, lambda x, y: x >= y)
co2 = readings(puz, lambda x, y: x < y)

print("Part2:", oxygen, co2, oxygen*co2)
