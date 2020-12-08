# def find_outer_bags(colour):
#     bags = []
#     for rule in rules:
#         for i, colours in enumerate(rule):
#             if i != 0 and colour in colours:
#                 bags.append(rule)
#     return bags

# def find_inner_bags(colour):
#     bags = []
#     colour = ''.join([i for i in colour if not i.isdigit()])
#     print("colour:", colour)
#     for rule in rules:
#         for i, colours in enumerate(rule):
#             if i == 0 and colour in colours:
#                 bags.append(rule)
#     return bags

# def find_new_outer_bags(bags):
#     for bag in bags:
#         new_bags = find_outer_bags(bag[0])
#         for new_bag in new_bags:
#             if new_bag not in bags:
#                 bags.append(new_bag)
#     return bags

# def find_new_inner_bags(bags):
#     for bag in bags:
#         if bag != bag[0]:
#             new_bags = find_inner_bags(bag)
#             for new_bag in new_bags:
#                 if new_bag not in bags:
#                     bags.append(new_bag)
#     return bags


# with open('Day 7/test2.txt') as file:
#     rules = []
#     for line in file:
#         line = line.rstrip().replace('.', '').replace('bags', 'bag').split(' contain ')
#         rules.append(line)

#     bags1 = find_outer_bags('shiny gold bag')
#     bags2 = find_inner_bags('shiny gold bag')

#     outer_bags = find_new_outer_bags(bags1)
#     inner_bags = find_new_inner_bags(bags2)

#     print(outer_bags)
#     print(len(outer_bags))  

#     print(inner_bags)
#     print(len(inner_bags))
data = [line.strip() for line in open("Day 7/input.txt", 'r')]


def solve1(data):
    rules = {}
    for d in data:
        #remove contian from data
        x = d[:-1].split(' contain ')
        #get the starting colour
        currentColor = x[0][:-5]
        for bag in x[1].split(', '):
            #if the bag can is the end and not recoreded, add them to the set(conditions)
            if bag != 'no other bags':
                color = ' '.join(bag.split(' ')[1:-1])
                if color not in rules:
                    #if end, add colour to the set of rules
                    rules[color] = set({})
                #otherwize add to the set if it doesnt exist
                rules[color].add(currentColor)

    colors = {'shiny gold'}
    added = True
    while added:
        added = False
        l = len(colors)
        #if the "shiny gold" can be contained 
        for color in colors:
            if color in rules:
                #see if its the final set or part of the larger condition
                colors = colors | rules[color]
        if len(colors) > l:
            added = True

    print(len(colors) - 1)
    
def solve2(data):
    rules = {}
    for d in data:
        #remove contain from data
        x = d[:-1].split(' contain ')
        #get the starting colour
        currentColor = x[0][:-5]
        #get the bags that can be contained
        for b in x[1].split(', '):
            if b != 'no other bags':
                #if end, add colour to the set of rules
                color = ' '.join(b.split(' ')[1:-1])
                num = int(b.split(' ')[0])
                if currentColor not in rules:
                    rules[currentColor] = set({})
                #otherwize add to the set if it doesnt exist
                rules[currentColor].add((color, num))
            else:
                #otherwize add on to the set
                rules[currentColor] = set({})

    def add_colors(color):
        total = 0
        
        for o_color, num in rules[color]:
            total += num * (1 + add_colors(o_color))
        return total

    print(add_colors('shiny gold'))



solve1(data)
solve2(data)