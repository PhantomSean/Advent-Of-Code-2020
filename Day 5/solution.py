with open("Day 5/input.txt") as file:
    lines = [list(line.rstrip()) for line in file]

test_lines = [ ['B','F','F','F','B','B','F','R','R','R'],
          ['F','F','F','B','B','B','F','R','R','R'],
          ['B','B','F','F','B','B','F','R','L','L']]
seat_ids = []
for line in lines:
    row_upper = 127
    row_lower = 0
    col_upper = 7
    col_lower = 0
    row = 0
    col = 0
    for i, letter in enumerate(line):
        if (letter == 'F'):
            row_upper = int((row_upper+1+row_lower)/2)-1
            if (i == 6):
                row = row_upper
        elif (letter == 'B'):
            row_lower = int((row_upper+1+row_lower)/2)
            if (i == 6):
                row = row_lower
        elif (letter == 'R'):
            col_lower = int((col_upper+1+col_lower)/2)
            if (i == 9):
                col = col_upper
        elif (letter == 'L'):
            col_upper = int((col_upper+1+col_lower)/2)-1
            if (i == 9):
                col = col_lower
    seat_ids.append((row*8)+col)
seat_ids.sort()
print(seat_ids[-1])

for i, line in enumerate(seat_ids):
    if (i+1 != len(seat_ids) and line+1 != seat_ids[i+1]):
        print(line+1)
