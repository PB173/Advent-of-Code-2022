import math

# Part 1
with open('day3.txt', 'r') as f:
    lines = f.readlines()

score = 0
for line in lines:
    line = line[0:-1]
    parts = (line[0:math.ceil(len(line)/2)], line[math.ceil(len(line)/2):])
    list1, list2 = list(parts[0]), list(parts[1])
    list1.sort(), list2.sort()

    unique_list1, unique_list2 = set(list1), set(list2)

    for l in unique_list1:
        if l in unique_list2:
            if l.islower():
                score += ord(l)-96
            else:
                score += ord(l)-38
    
print("Answer of part 1:",score)

# part 2 
score = 0
for ind in range(0,len(lines),3):
    group = lines[ind:ind+3]
    unique_list = []
    for line in group:
        line = line[0:-1]
        list_line = list(line)
        list_line.sort()
        unique_list.append(set(list_line))


    sorted_unique_list = sorted(unique_list,key=len)
    for l in sorted_unique_list[0]:
        if l in sorted_unique_list[1] and l in sorted_unique_list[2]:
            if l.islower():
                print(l, ord(l)-96)
                score += ord(l)-96
            else:
                print(l, ord(l)-38)
                score += ord(l)-38

print("Answer of part 2:",score)








