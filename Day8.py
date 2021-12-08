# define a seven segment clock

sevenSegments = [
    ["a", "b", "c", "e", "f", "g"],
    ["c", "f"],
    ["a", "c", "d", "e", "g"],
    ["a", "c", "d", "f", "g"],
    ["b", "c", "d", "f"],
    ["a", "b", "d", "f", "g"],
    ["a", "b", "d", "e", "g"],
    ["a", "c", "f"],
    ["a", "b", "c", "d", "e", "f", "g"],
    ["a", "b", "c", "d", "f", "g"]
]

# import puzzel
puz = [puz.split("|") for puz in open("./puzzles/day8_example")]
digital = [(line[0].strip().split(" "), line[1].strip().split(" "))
           for line in puz]

# part 1
uniqueSevenSegments = [
    ["c", "f"],
    ["b", "c", "d", "f"],
    ["a", "c", "f"],
    ["a", "b", "c", "d", "e", "f", "g"]
]
uniqueSevenSegmentsLen = set([len(x) for x in uniqueSevenSegments])

sevenSegmentsMap = {len(x): (i, x) for i, x in enumerate(sevenSegments)}


def countUniqueSegments(digital, partIndex):
    return sum([1 for output in digital for num in output[partIndex]
                if len(num) in uniqueSevenSegmentsLen])


print("Part1", countUniqueSegments(digital, 1))

# part 2


def decodeSignalWiring(panel):
    translation = {}
    for digit in panel:
        if len(digit) in uniqueSevenSegmentsLen:
            origNum = sevenSegmentsMap[len(digit)]
            print(digit, origNum)
            for char, orig in zip(digit, origNum[1]):
                print(char, orig)
                if char in translation.keys():
                    # todo: some bug here where we have multiple duplicates if we try to only match the unique ones
                    print("ERROR DUPLICATE MAPPING", char, orig)
                translation[char] = orig
    return translation


def translateSignal(panel, transMap):
    for digit in panel:
        newDigit = [transMap[char] for char in digit]
        for num in transMap:
            # todo: check if all chars are in the array -> we match the number
            if all(newDigit, lambda char: char in num[1]):
                print(num[0])
        print("---")


translationMap = decodeSignalWiring(digital[0][0])
# translateSignal(digital[0][1], translationMap)
