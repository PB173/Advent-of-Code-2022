# Part 1
with open('day4.txt', 'r') as f:
    lines = f.readlines()

overlap = 0
for line in lines:
    split_line = line.split(",")
    section_1, section_2 = split_line[0].split("-"), split_line[1].split("-")
    start_1, start_2, end_1, end_2 = int(section_1[0]), int(section_2[0]), int(section_1[1]), int(section_2[1])

    if start_2 in range(start_1, end_1+1) and end_2 in range(start_1, end_1+1) or \
        start_1 in range(start_2, end_2+1) and end_1 in range(start_2, end_2+1):
        overlap += 1
    
print("Part 1:",overlap)

# Part 2
overlap = 0
for line in lines:
    split_line = line.split(",")
    section_1, section_2 = split_line[0].split("-"), split_line[1].split("-")
    start_1, start_2, end_1, end_2 = int(section_1[0]), int(section_2[0]), int(section_1[1]), int(section_2[1])

    if start_2 <= end_1 and start_2 >= start_1 or start_1 <= end_2 and start_1 >= start_2:
        overlap +=1

print("Part 2:",overlap)




