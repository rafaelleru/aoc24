import re

# input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
regex = r"mul\((\d{,3},\d{,3})\)"

f = open("input.txt", "r")
input = f.read().strip()
f.close()

sum = 0
for match in re.finditer(regex, input):
    a, b = match.group(1).split(",")
    sum += int(a) * int(b)

print(f"Sol 1: {sum}")

default_regex = r"mul\((\d{,3},\d{,3})\)"

# input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
enabled = True
start = 0
end = input.find("don't()", start)
substr_end = input.find("don't()")
endofstr = False
sum2 = 0

while not endofstr:
    if enabled:
        for match in re.finditer(regex, input[start:end]):
            a, b = match.group(1).split(",")
            sum2 += int(a) * int(b)

    if enabled:
        start = end + 7
        end = input.find("do()", start)
    else:
        start = end + 3
        end = input.find("don't()", start)

    enabled = not enabled

    if end == -1:
        endofstr = True


for match in re.finditer(regex, input[start:end]):
    if enabled:
        a, b = match.group(1).split(",")
        sum2 += int(a) * int(b)

print(f"Sol2: {sum2}")


# This is quite more elegant
# regex = r"mul\(\d{,3},\d{,3}\)|do\(\)|don't\(\)"
# sum2 = 0
# flag = True

# for match in re.findall(regex, input):
    # if match == "do()":
        # flag = True
    # elif match == "don't()":
        # flag = False
    # else:
        # if flag:
            # a, b = map(int, match[4:-1].split(","))
            # sum2 += a * b

# print(sum2)
