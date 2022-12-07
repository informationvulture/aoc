"""
AoC Day 3 2022
"""

def get_rucksack_item():
    """
    TO DO
    """
    priority_sum = 0
    with open("3_input.txt", "r", encoding="utf-8") as rucksacks:
        for rucksack in rucksacks:

            # Get the one unique item in the first and second half
            # of the rucksack.
            unique_item = list(set(rucksack[0:len(rucksack)//2]) \
            & set(rucksack[len(rucksack)//2:]))[0]
            
            if unique_item.isupper():
                priority_sum += ord(unique_item) - 38
            else:
               priority_sum += ord(unique_item) - 96
    return priority_sum 

def get_three_group_item():
    """
    TO DO
    """
    priority_sum = 0
    with open("3_input.txt", "r", encoding="utf-8") as rucksacks:
        elf_group = []
        for elf, rucksack in enumerate(rucksacks):

            # Find out if it's the 3rd elf, meaning
            # the group is now finished.
            if (elf + 1) % 3 == 0:
                elf_group.append(rucksack.strip())
                unqiue_item = list(set(elf_group[0]) \
                & set(elf_group[1]) & set(elf_group[2]))[0]

                if unqiue_item.isupper():
                    priority_sum += ord(unqiue_item) - 38
                else:
                    priority_sum += ord(unqiue_item) - 96
                elf_group = []
            else:
                elf_group.append(rucksack.strip())
    return priority_sum


def main():
    """
    Main function
    """
    # Part 1
    priority_sum = get_rucksack_item()
    print(f"Priority sum: {priority_sum}")

    # Part 2
    three_groups_sum = get_three_group_item()
    print(f"Three groups sum: {three_groups_sum}")

if __name__ == "__main__":
    main()