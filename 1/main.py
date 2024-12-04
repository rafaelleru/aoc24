from collections import defaultdict

with open('input.txt') as file:
    input = file.read().strip().split('\n')


list1 = []
list2 = []
for line in input:
    d1, d2 = line.split('  ')
    list1.append(int(d1))
    list2.append(int(d2))

list1.sort()
list2.sort()

# Iterate over list1, list2 at the same time

total_dist = 0

for i in range(len(list1)):
    total_dist += abs(list1[i]-list2[i])

print(f"Sol 1: {total_dist}")

similarity_score = defaultdict(lambda: 0)

for i in range(len(list1)):
    val = list1[i]
    for j in range(len(list2)):
        if list2[j] == val:
            similarity_score[val] += 1


total_similarity_score = 0
for k, v in similarity_score.items():
    total_similarity_score += k*v


print(total_similarity_score)

