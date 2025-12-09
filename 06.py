FILENAME = "06_input.txt"

def task1():
    with open(FILENAME) as f:
        lines: list[str] = f.readlines()
        problems: list[list[str]] = []
        for line in lines:
            problems.append(line.strip().replace("  ", " ").replace(" ", ",").replace(",,", ",").replace(",,", ",").split(","))
        width: int = len(problems[0])
        height: int = len(problems)-1 # because last one is the operator

    for line in problems:
        for thing in line:
            thing.strip(" ")
            if thing == " ":
                line.remove(thing)
            

    result: int = 0
    for i in range(width):
        subtotal: int = 0
        match problems[-1][i]:
            case "+":
                subtotal = 0
                for k in range(height):
                    subtotal += int(problems[k][i])
            case "*":
                subtotal = 1
                for k in range(height):
                    subtotal *= int(problems[k][i])
        
        result += subtotal
    
    return result


def task2():
    with open(FILENAME) as f:
        lines: list[str] = f.readlines()
        for line in lines:
            line = line.strip("\n")

    result: int = 0

    i: int = 0
    while i < len(lines[-1]):

        if i >= len(lines[-1])-5:
            pass

        k: int = i
        subtotal: int = 1 if lines[-1][i] == "*" else 0
        while k < len(lines[-1]) and (k == i or lines[-1][k] == " "):
            if k != i and k < len(lines[-1]) and lines[-1][k+1] != " " and lines[-1][k+1] != "\n":
                break

            num: int = 0
            for n in range(len(lines)-1):
                if lines[n][k] != " " and lines[n][k] != "\n":
                    num *= 10
                    num += int(lines[n][k])
            if lines[-1][i] == "*":
                subtotal *= num
            else:
                subtotal += num

            k += 1

        result += subtotal
        i = k+1

    return result


print(f"The code to day 6 part 1 is: {task1()}")
print(f"The code to day 6 part 2 is: {task2()}")