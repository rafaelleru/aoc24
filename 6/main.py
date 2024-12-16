def move(guard_position, direction):
    moves = {
        "N": (-1, 0),
        "E": (0, 1),
        "S": (1, 0),
        "W": (0, -1)
    }
    new_pos = guard_position[0] + moves[direction][0], guard_position[1] + moves[direction][1]
    return new_pos


def in_map(position, map):
    return 0 <= position[0] < len(map) and 0 <= position[1] < len(map[0])


input = open('./input.txt')
map = [x.strip() for x in input.readlines()]
direction = 'N'
visited = set()
rotations = {
    "N": "E",
    "E": "S",
    "S": "W",
    "W": "N"
}

# Parse the input
for x in range(len(map)):
    for y in range(len(map[0])):
        if map[x][y] == '^':
            guard_position = (x, y)

visited.add(guard_position)

while True:
    new_pos = move(guard_position, direction)
    if not in_map(new_pos, map):
        break

    if map[new_pos[0]][new_pos[1]] == '#':
        direction = rotations[direction]
    else:
        guard_position = new_pos
        visited.add(guard_position)

print(len(visited))
