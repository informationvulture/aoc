"""
AoC 2018 Day 2
"""
from collections import Counter

def extract_box_id():
    twos = 0
    threes = 0
    with open("2_input.txt", "r", encoding="utf-8") as box_ids:
        for box_id in box_ids:
            vals = sorted(Counter(box_id.strip()).items(), key=lambda x: x[1], reverse=True)[0:2]
            nums = [i[1] for i in vals]
            twos += 1 if 2 in nums else 0
            threes += 1 if 3 in nums else 0
    return twos * threes


def main():
    # Part 1
    vals = extract_box_id()
    print(f"Checksum: {vals}")

    # Part 2 is incomplete
    

if __name__ == "__main__":
    main()