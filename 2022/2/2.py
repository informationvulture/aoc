"""
Day 2 of AoC 2022
"""


def get_score(updated=False):
    """
    Uses two hashmaps to get the score, depending on
    if the user wants the updated score (part 2) based on the new
    info from the elf, or the original score (part 1).
    """
    tally = 0
    score_hashmap = {
        "AX": 4,
        "BX": 1,
        "CX": 7,
        "AY": 8,
        "BY": 5,
        "CY": 2,
        "AZ": 3,
        "BZ": 9,
        "CZ": 6
    }
    updated_score_hashmap = {
        "AX": 3,
        "BX": 1,
        "CX": 2,
        "AY": 4,
        "BY": 5,
        "CY": 6,
        "AZ": 8,
        "BZ": 9,
        "CZ": 7
    }
    with open("2_input.txt", "r", encoding="utf-8") as rounds:
        if not updated:
            for round in rounds:

                # We had to use .strip() to remove the newline character
                tally += score_hashmap["".join(round.strip().split(" "))]
        else:
            for round in rounds:
                tally += updated_score_hashmap["".join(round.strip().split(" "))]

    return tally

def main():

    tally = get_score()

    print(f"Total score is {tally}")

    tally = get_score(updated=True)

    print(f"Total updated score is {tally}")

if __name__ == "__main__":
    main()
