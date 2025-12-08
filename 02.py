FILENAME = "02_input.txt"

def task1():
    result: int = 0

    with open(FILENAME) as f:
        line: str = f.readline()

    seqs: list[str] = line.split(",")
    for seq in seqs:
        ids: list[str] = seq.split("-")
        # not a very clever solution; there may be a better way of
        # doing this than brute force, but I haven't found it yet
        for id in range(int(ids[0]), int(ids[1])+1):
            if not is_valid_1(str(id)):
                result += int(id)
    
    return result


def task2():
    result: int = 0

    with open(FILENAME) as f:
        line: str = f.readline()

    seqs: list[str] = line.split(",")
    for seq in seqs:
        ids: list[str] = seq.split("-")
        for id in range(int(ids[0]), int(ids[1])+1):
            # ditto as before, only even more grossly inefficient
            if not is_valid_2(str(id)):
                result += int(id)
    
    return result


def is_valid_1(id: str):
    return id[:len(id)//2] != id[len(id)//2:]


def is_valid_2(id: str):
    for i in range(1, len(id)):
        if id == id[:i] * (len(id) // i):
            return False
    return True

print(f"The code to day 2 part 1 is: {task1()}")
print(f"The code to day 2 part 2 is: {task2()}")
