import numpy as np

# Part 1
with open('day1.txt', 'r') as f:
    lines = f.readlines()
    
sum_per_elf = 0
cal = []
for line in lines:
    if line.strip():
        sum_per_elf += int(line)
    else:
        cal.append(sum_per_elf)
        sum_per_elf = 0

max_elf = np.max(cal)
print(max_elf)

# part 2
cal.sort()
n = len(cal)
max_3_elf = sum(cal[n-3:n])
print(max_3_elf)

