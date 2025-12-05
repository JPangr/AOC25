FILENAME = "03_input.txt"

def task1(FILENAME):
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

print(f"The code to day 3 part 1 is: {task1(FILENAME)}")
