XAXIS = "ABCDEFGH"
YAXIS = "12345678"

FORBIDDEN = {
    "B1": ["up"],
    "E1": ["right"],
    "F1": ["left"],
    "B2": ["down"],
    "C2": ["right"],
    "D2": ["left"],
    "F2": ["right"],
    "G2": ["left"],
    "D3": ["up"],
    "H3": ["up"],
    "D4": ["down"],
    "F4": ["right"],
    "G4": ["left"],
    "H4": ["down"],
    "E5": ["up"],
    "G5": ["up"],
    "A6": ["up"],
    "E6": ["down"],
    "G6": ["down"],
    "A7": ["down"],
    "B7": ["right"],
    "C7": ["left", "right"],
    "D7": ["left"],
    "F7": ["up"],
    "A8": ["right"],
    "B8": ["left"],
    "F8": ["down", "right"],
    "G8": ["left"],

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

    while can_move(current, "up"):
        current = move(current, "up")

    while can_move(current, "left"):
        current = move(current, "left")


    while can_move(current, "down"):
        current = move(current, "down")
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