puzzle = []


def find_diagonal_right_up(position, puzzle):
    found = False
    x = position[0]
    y = position[1]

    if x - 3 >= 0 and y + 3 < len(puzzle[0]):
        found = puzzle[x - 1][y + 1] == 'M' and puzzle[x - 2][y + 2] == 'A' and puzzle[x - 3][y + 3] == 'S'
        if found:
            # print("diag rigth up")
            pass
    else:
        found = False

    return found


def find_diagonal_left_up(position, puzzle):
    found = False
    x = position[0]
    y = position[1]

    if x - 3 >= 0 and y - 3 >= 0:
        found = puzzle[x - 1][y - 1] == 'M' and puzzle[x - 2][y - 2] == 'A' and puzzle[x - 3][y - 3] == 'S'
        if found:
            # print("diag left up")
            pass
    else:
        found = False

    return found


def find_diagonal_left_down(position, puzzle):
    found = False
    x = position[0]
    y = position[1]

    if x + 3 < len(puzzle) and y - 3 >= 0:
        found = puzzle[x + 1][y - 1] == 'M' and puzzle[x + 2][y - 2] == 'A' and puzzle[x + 3][y - 3] == 'S'
        if found:
            # print("diag left down")
            pass
    else:
        found = False

    return found


def find_diagonal_right_down(position, puzzle):
    found = False
    x = position[0]
    y = position[1]

    if x + 3 < len(puzzle) and y + 3 < len(puzzle[0]):
        found = puzzle[x + 1][y + 1] == 'M' and puzzle[x + 2][y + 2] == 'A' and puzzle[x + 3][y + 3] == 'S'
        if found:
            # print("diag rigth down")
            pass
    else:
        found = False

    return found


def find_down(position, puzzle):
    found = False
    x = position[0]
    y = position[1]

    if x + 3 < len(puzzle):
        found = puzzle[x + 1][y] == 'M' and puzzle[x + 2][y] == 'A' and puzzle[x + 3][y] == 'S'
        if found:
            # print("down")
            pass
    else:
        found = False

    return found


def find_up(position, puzzle):
    found = False
    x = position[0]
    y = position[1]

    if x - 3 >= 0:
        found = puzzle[x - 1][y] == 'M' and puzzle[x - 2][y] == 'A' and puzzle[x - 3][y] == 'S'
        if found:
            # print("up")
            pass
    else:
        found = False

    return found


def find_left(position, puzzle):
    found = False
    x = position[0]
    y = position[1]

    if y - 3 >= 0:
        found = puzzle[x][y - 1] == 'M' and puzzle[x][y - 2] == 'A' and puzzle[x][y - 3] == 'S'
        if found:
            # print("left")
            pass
    else:
        found = False

    return found


def find_right(position, puzzle):
    found = False
    x = position[0]
    y = position[1]

    if y + 3 < len(puzzle[0]):
        found = puzzle[x][y + 1] == 'M' and puzzle[x][y + 2] == 'A' and puzzle[x][y + 3] == 'S'
        if found:
            pass
            # print("rigth")
            pass
    else:
        found = False

    return found


with open('input.txt', 'r') as input:
    for line in input.readlines():
        row = [char for char in line.strip()]
        puzzle.append(row)

count = 0
diag = 0
for x in range(len(puzzle)):
    for y in range(len(puzzle[0])):
        if puzzle[x][y] == 'X':
            if find_right((x, y), puzzle):
                count += 1
            if find_left((x, y), puzzle):
                count += 1
            if find_up((x, y), puzzle):
                count += 1
            if find_down((x, y), puzzle):
                count += 1
            if find_diagonal_left_up((x, y), puzzle):
                count += 1
                diag += 1
            if find_diagonal_right_up((x, y), puzzle):
                count += 1
                diag += 1
            if find_diagonal_left_down((x, y), puzzle):
                count += 1
                diag += 1
            if find_diagonal_right_down((x, y), puzzle):
                count += 1
                diag += 1

# print(diag)
print(count)


# Part 2

def find_xMAS(position, puzzle):
    found = False
    x = position[0]
    y = position[1]

    if x - 1 >= 0 and x + 1 < len(puzzle) and y - 1 >= 0 and y + 1 < len(puzzle[0]):
        if (puzzle[x - 1][y - 1] == 'M' and puzzle[x - 1][y + 1] == 'S' and puzzle[x + 1][y - 1] == 'M' and puzzle[x + 1][y + 1] == 'S'):
            found = True
        elif (puzzle[x - 1][y - 1] == 'S' and puzzle[x - 1][y + 1] == 'S' and puzzle[x + 1][y - 1] == 'M' and puzzle[x + 1][y + 1] == 'M'):
            found = True
        elif (puzzle[x - 1][y - 1] == 'M' and puzzle[x - 1][y + 1] == 'M' and puzzle[x + 1][y - 1] == 'S' and puzzle[x + 1][y + 1] == 'S'):
            found = True
        elif (puzzle[x - 1][y - 1] == 'S' and puzzle[x - 1][y + 1] == 'M' and puzzle[x + 1][y - 1] == 'S' and puzzle[x + 1][y + 1] == 'M'):
            found = True

    return found


count = 0
for x in range(len(puzzle)):
    for y in range(len(puzzle[0])):
        if puzzle[x][y] == 'A':
            if find_xMAS((x, y), puzzle):
                count += 1

print(count)
