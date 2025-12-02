FILENAME: str = "01_input.txt"
START: int = 50

def task1(FILENAME, START):
    position: int = START
    zero_count: int = 0

    with open(FILENAME) as f:
        lines: list[str] = f.readlines()
        for line in lines:
            line = line.strip("\n")

            rotation: tuple[int, int] = parse(line)
            direction, clicks = rotation

            position += (direction * clicks) % 100
            position %= 100

            if position == 0:
                zero_count += 1

    return zero_count
            

def parse(line: str):
    r1: int
    r2: int

    r1 = 1 if line[0] == "R" else -1
    r2 = int(line[1:])

    return (r1, r2)

print(f"The code to day 1 part 1 is: {task1(FILENAME, START)}")