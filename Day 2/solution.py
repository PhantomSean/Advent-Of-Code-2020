def check_in_range(password, letter, start, stop):
    count = password.count(letter)
    return count >= start and count <= stop

def check_index(password, letter, start, stop):
    return (password[start] == letter or password[stop] == letter) and (password[start] != password[stop])

with open("Day 2/input.txt") as file:
    letters = [num.split(": ") for num in file]
    count1 = 0
    count2 = 0
    for policy, password in letters:
        length, letter = policy.split(" ")
        start, stop = length.split("-")
        start, stop = int(start), int(stop)

        # part 1
        if check_in_range(password, letter, start, stop): count1 +=1

        # part 2
        if check_index(password, letter, start-1, stop-1): count2 +=1

print(count1)
print(count2)