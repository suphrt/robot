XAXIS = "ABCDEFGH"
YAXIS = "12345678"

FORBIDDEN = {
    "G1": ["up"],
    "A2": ["right"],
    "B2": ["left"],
    "E2": ["up"],
    "G2": ["down"],
    "E3": ["down"],
    "D4": ["up"],
    "G4": ["right"],
    "H4": ["left"],
    "C5": ["up"],
    "D5": ["down"],
    "B6": ["up"],
    "C6": ["down"],
    "F6": ["right"],
    "G6": ["left"],
    "H6": ["up"],
    "B7": ["down"],
    "H7": ["down"],
    "E8": ["right"],
    "F8": ["left"],
}

def move(position, direction):
    i = XAXIS.index(position[0])
    j = YAXIS.index(position[1])

    if direction == "left":
        if i > 0:
            return XAXIS[i - 1] + position[1]

    elif direction == "right":
        if i < len(XAXIS) - 1:
            return XAXIS[i + 1] + position[1]

    elif direction == "up":
        if j < len(YAXIS) - 1:
            return position[0] + YAXIS[j + 1]

    elif direction == "down":
        if j > 0:
            return position[0] + YAXIS[j - 1]

    return position


def can_move(position, direction):
    if position[0] == "A" and direction == "left":
        return False

    elif position[0] == "H" and direction == "right":
        return False

    elif position[1] == "8" and direction == "up":
        return False

    elif position[1] == "1" and direction == "down":
        return False

    rules = FORBIDDEN.get(position, [])
    return direction not in rules


def execute(start):
    current = start
    while can_move(current, "right"):
        current = move(current, "right")

    while can_move(current, "down"):
        current = move(current, "down")

    while can_move(current, "left"):
        current = move(current, "left")

    while can_move(current, "up"):
        current = move(current, "up")

    return current


if __name__ == "__main__":
    result = []

    for x in XAXIS:
        for y in YAXIS:
            start = x + y
            finish = execute(start)
            if start == finish:
                result.append(start)

    print(len(result))
    print(", ".join(result))