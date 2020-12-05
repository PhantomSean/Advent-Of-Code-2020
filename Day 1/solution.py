with open("input.txt") as file:
    line = [int(x.strip()) for x in file]

for i, n1 in enumerate(line):
    for j, n2 in enumerate(line[i+1:]):
        if n1 + n2 == 2020:
            part1 = n1 * n2
        for n3 in line[i+j+1:]:
            if n1 + n2 + n3 == 2020:
                part2 = n1 * n2 * n3

print(part1)
print(part2)