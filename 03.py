FILENAME = "03_input.txt"

def task1():
    result: int = 0
    with open(FILENAME) as f:
        lines: list[str] = f.readlines()
    
    for line in lines:
        line = line.strip("\n")
        first: int = 0
        for i in range(len(line)-1):
            if ord(line[i]) > ord(line[first]):
                first = i
        
        second: int = first+1
        for i in range(first+1, len(line)):
            if ord(line[i]) > ord(line[second]):
                second = i
        
        result += 10*int(line[first]) + int(line[second])

    return result


def task2():
    result: int = 0
    with open(FILENAME) as f:
        lines: list[str] = f.readlines()
    
    for line in lines:
        line = line.strip("\n")
        
        positions: list[int] = 12 * [0]

        # looks a little convoluted, but is actually pretty simple
        # we find the position P0 with the greatest value in the range [0..n]
        # then we look for the position P1, in the range [P0+1..n+1]
        # then P2, in the range [P1..n+2]
        # etc
        # where n is length of our input minus the desired length of our output + 1
        prev = -1
        for i in range(12):
            positions[i] = prev+1
            for k in range(prev+1, len(line) - (11-i)):
                if ord(line[k]) > ord(line[positions[i]]):
                    positions[i] = k
            prev = positions[i]

        thing = ""
        for i, pos in enumerate(positions):
            thing += line[pos]
            result += int(line[pos]) * (10 ** (11-i))

        assert(True)

    return result

print(f"The code to day 3 part 1 is: {task1()}")
print(f"The code to day 3 part 2 is: {task2()}")
