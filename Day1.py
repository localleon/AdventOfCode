# import puzzel
puz = [int(line.strip("\n")) for line in open("./puzzles/day1_final")]

# solve puzzel part 1
res = sum(mes > puz[i] for i, mes in enumerate(puz[1:]))
print(res)

# part 2
windows = [sum([mes, puz[i+1], puz[i+2]]) for i, mes in enumerate(puz[:-2])]
res2 = sum(mes > windows[i] for i, mes in enumerate(windows[1:]))
print(res2)
