FILENAME = "07_input.txt"

def task1():
    with open(FILENAME) as f:
        lines: list[list[str]] = [list(line) for line in f.readlines()]
    
    result: int = 0
    for i in range(1, len(lines)):
        for k in range(len(lines[i])):
            if lines[i-1][k] == "S" or lines[i-1][k] == "|":
                if lines[i][k] == ".":
                    lines[i][k] = "|"
                elif lines[i][k] == "^":
                    if k > 0:
                        lines[i][k-1] = "|"
                    if k < len(lines)-1:
                        lines[i][k+1] = "|"
                    result += 1
    return result


print(f"The code to day 7 part 1 is: {task1()}")
