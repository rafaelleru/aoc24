from collections import defaultdict

page_ordering_rules_graph = defaultdict(set)
page_orderings = []
print_rules = []
valid_rules = []
invalid_rules = []
broken_rules = []


def is_valid_printing(rule, i):
    for x in range(0, i):
        if rule[x] in page_ordering_rules_graph[rule[i]]:
            broken_rules.append({"wrong_idx": x, "rule": rule})
            return False

    return True


with open('input.txt', 'r') as input:
    for line in input.readlines():
        if "|" in line:
            a, b = map(int, line.strip().split("|"))
            page_orderings.append((a, b))
        elif "," in line:
            print_rule = [int(x) for x in line.strip().split(",")]
            print_rules.append(print_rule)


for porder in page_orderings:
    page_ordering_rules_graph[porder[0]].add(porder[1])

for rule in print_rules:
    valid = True
    for i in range(len(rule)):
        if not is_valid_printing(rule, i):
            valid = False
            break

    if valid:
        valid_rules.append(rule)
    # for part 2
    else:
        invalid_rules.append(rule)


# print(valid_rules)

sum = 0
for r in valid_rules:
    sum += r[len(r) // 2]

print(sum)

sum2 = 0

for rule in broken_rules:
    reordered = []
    rule["rule"][rule["wrong_idx"]], rule["rule"][rule["wrong_idx"] + 1] = rule["rule"][rule["wrong_idx"] + 1], rule["rule"][rule["wrong_idx"]]
    print(rule["rule"])



print(sum2)
