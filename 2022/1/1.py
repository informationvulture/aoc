"""
Day 1 of AoC 2022
"""

def count_calories():
    """
    Each elf is carrying food of a certain worth of calories,
    and is denoted by groups of numbers seperated by a newline.
    """
    values = [] # main values
    with open("1_input.txt", "r", encoding="utf-8") as elf_calories:
        elf = [] # values for each elf
        for line in elf_calories:
            if line == "\n": # elf is done
                values.append(sum(elf)) # add elf's total calories
                elf = [] # reset elf
            else:
                elf.append(int(line)) # add calories to elf
    return values

def main():
    elfs = count_calories()
    
    # For part 1
    print(f"Elf carrying the most Calories: {max(elfs)}")

    # For part 2
    print(f"Top three with most Calories {sum(sorted(elfs)[-3:])}")

if __name__ == "__main__":
    main()