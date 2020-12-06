from typing import Counter


with open("Day 6/input.txt") as file:
    groups = []
    group = []
    duplicate = []
    unique = 0
    same_ans = 0
    group_size = 0
    count = 0

    for line in file:
        if (line.strip()):
            for letter in line.strip():
                group.append(letter)
            count += 1
        elif (not line.strip()):
            group.append(count)
            groups.append(group)
            group = []
            count = 0
    group.append(count)
    groups.append(group)

    for group in groups:
        unique += len(set(group[:-1]))
        count = Counter(group[:-1])
        for letter in group:
            if (count[letter] == group[-1] and letter not in duplicate):
                duplicate.append(letter)
        same_ans += len(set(duplicate))
        duplicate = []

    print(unique)
    print(same_ans)