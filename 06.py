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


print(f"The code to day 6 part 1 is: {task1()}")
