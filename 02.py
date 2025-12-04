FILENAME = "02_input.txt"

def task1(FILENAME):
    result: int = 0

    with open(FILENAME) as f:
        line: str = f.readline()

    seqs: list[str] = line.split(",")
    for seq in seqs:
        ids: list[str] = seq.split("-")
        # not a very clever solution; there may be a better way of
        # doing this than brute force, but I haven't found it yet
        for id in range(int(ids[0]), int(ids[1])+1):
            if not is_valid(str(id)):
                result += int(id)
    
    return result


def is_valid(id: str):
    return id[:len(id)//2] != id[len(id)//2:]

print(f"The code to day 2 part 1 is: {task1(FILENAME)}")
