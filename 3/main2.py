import re

# Input string
input_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# Initial state
enabled = True
start = 0
sum2 = 0

# Regex to find `mul(x,y)` operations
regex = r"mul\((\d+),(\d+)\)"

while start < len(input_str):
    # Find the next control operation ("don't()" or "do()")
    dont_pos = input_str.find("don't()", start)
    do_pos = input_str.find("do()", start)

    # Determine the next control operation and its position
    if dont_pos == -1 and do_pos == -1:
        end = len(input_str)  # No more control operations
    elif dont_pos == -1:
        end = do_pos
    elif do_pos == -1:
        end = dont_pos
    else:
        end = min(dont_pos, do_pos)

    # If enabled, process `mul` operations in the current segment
    if enabled:
        for match in re.finditer(regex, input_str[start:end]):
            a, b = map(int, match.groups())
            sum2 += a * b

    # Exit if no more control operations are found
    if end == len(input_str):
        break

    # Update `enabled` based on the encountered control operation
    if input_str[end:end + 7] == "don't()":
        enabled = False
        start = end + 7
    elif input_str[end:end + 3] == "do()":
        enabled = True
        start = end + 3

# Process the remaining part of the string if enabled
if enabled:
    for match in re.finditer(regex, input_str[start:]):
        a, b = map(int, match.groups())
        sum2 += a * b

# Print the result
print(sum2)
