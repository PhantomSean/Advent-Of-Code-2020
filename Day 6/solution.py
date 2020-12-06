from collections import Counter

with open("Day 6/input.txt") as file:
    group_size = 0
    unique = 0
    same_answers = 0
    group_answers = []
    for line in file:
        if(line != "\n"):
            line = line.rstrip()
            group_size += 1
            group_answers += line
        elif(line == "\n"):
            duplicate = []
            count = Counter(group_answers)
            for letter in group_answers:
                if (count[letter] == group_size and (letter not in duplicate)):
                    duplicate += letter
            unique += len(set(group_answers))
            same_answers += len(set(duplicate))
            group_size = 0
            group_answers = []
    print(unique)
    print(same_answers)