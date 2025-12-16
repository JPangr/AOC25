from math import inf as INT_MAX, sqrt

FILENAME = "08_input.txt"

def task1():
    positions: list[tuple[int, int, int]] = []
    circuits: list[set[tuple[int, int, int]]] = []

    with open(FILENAME) as f:
        for line in f.readlines():
            pos: list[str] = line.split(",")
            positions.append((int(pos[0]), int(pos[1]), int(pos[2])))

    distances: list[tuple[tuple[int, int, int], tuple[int, int, int], float]] = []
    for i in range(len(positions)-1):
        for k in range(i+1, len(positions)):
            distances.append((positions[i], positions[k], distance(positions[i], positions[k])))
    distances.sort(key = (lambda x: x[2]))

    for i in range(1000):
        p1, p2, _ = distances[i]
        connected: bool = False
        prev = None
        for circuit in circuits:
            if p1 in circuit or p2 in circuit:
                if connected:
                    assert(prev is not None)
                    circuit.update(prev)
                    circuits.remove(prev)
                circuit.add(p1)
                circuit.add(p2)
                connected = True
                prev = circuit
        if not connected:
            circuits.append({p1, p2})

    a: int = 1
    b: int = 1
    c: int = 1
    for circuit in circuits:
        ln: int = len(circuit)
        if ln > a:
            c = b
            b = a
            a = ln
        elif ln > b:
            c = b
            b = ln
        elif ln > c:
            c = ln

    return a*b*c


def task2():
    positions: list[tuple[int, int, int]] = []
    circuits: list[set[tuple[int, int, int]]] = []

    with open(FILENAME) as f:
        for line in f.readlines():
            pos: list[str] = line.split(",")
            positions.append((int(pos[0]), int(pos[1]), int(pos[2])))

    distances: list[tuple[tuple[int, int, int], tuple[int, int, int], float]] = []
    for i in range(len(positions)-1):
        for k in range(i+1, len(positions)):
            distances.append((positions[i], positions[k], distance(positions[i], positions[k])))
    distances.sort(key = (lambda x: x[2]))

    for i in range(len(distances)):
        p1, p2, _ = distances[i]
        connected: bool = False
        prev = None
        for circuit in circuits:
            if p1 in circuit or p2 in circuit:
                if connected:
                    assert(prev is not None)
                    circuit.update(prev)
                    circuits.remove(prev)
                circuit.add(p1)
                circuit.add(p2)
                connected = True
                prev = circuit
                if len(circuit) == len(positions):
                        return p1[0]*p2[0]
        if not connected:
            circuits.append({p1, p2})

    assert(False)


def distance(pos1: tuple[int, int, int], pos2: tuple[int, int, int]):
    return sqrt((pos1[0] - pos2[0])**2 +
                (pos1[1] - pos2[1])**2 +
                (pos1[2] - pos2[2])**2)


print(f"The code to day 8 part 1 is: {task1()}")
print(f"The code to day 8 part 2 is: {task2()}")