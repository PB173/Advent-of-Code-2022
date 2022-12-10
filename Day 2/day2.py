# Part 1
with open('day2.txt', 'r') as f:
    lines = f.readlines()

total = 0
for line in lines:
    split_line = line.split()
    elf_move, my_move = split_line[0], split_line[1]

    if elf_move == 'A': # Rock
        if my_move == 'X': # Rock
            score = 1+3
        elif my_move == 'Y': # Paper
            score = 2+6
        else: # Scissors
            score = 3+0
    elif elf_move == 'B': # Paper
        if my_move == 'X': # Rock
            score = 1+0
        elif my_move == 'Y': # Paper
            score = 2+3
        else: # Scissors
            score = 3+6
    else: # Scissors
        if my_move == 'X': # Rock
            score = 1+6
        elif my_move == 'Y': # Paper
            score = 2+0
        else: # Scissors
            score = 3+3
    total += score    

print("Answer of part 1:",total)

# Part 2 
total = 0

for line in lines:
    split_line = line.split()
    elf_move, result = split_line[0], split_line[1]

    if elf_move == 'A': # Rock
        if result == 'X': # Lose; you play scissors
            score = 3+0
        elif result == 'Y': # Draw; you play rock
            score = 1+3
        else: # Win; you play paper
            score = 2+6
    elif elf_move == 'B': # Paper
        if result == 'X': # Lose; you play rock
            score = 1+0
        elif result == 'Y': # Draw; you play paper
            score = 2+3
        else: # Win; you play scissors
            score = 3+6
    else: # Scissors
        if result == 'X': # Lose; you play paper
            score = 2+0
        elif result == 'Y': # Draw; you play scissors
            score = 3+3
        else: # Win; you play rock
            score = 1+6
    total += score   

print("Answer of part 2:",total)




