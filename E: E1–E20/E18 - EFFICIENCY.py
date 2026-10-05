"""E18 - EFFICIENCY"""

from math import ceil

def main():
    """Main Function"""
    total, big = 0, 0

    for w in range(int(input())):
        work = ceil(int(input()) / 12)
        total += work
        if work > 10:
            big += 1
            print("JOB", w + 1, work, "BIG")
        else:
            print("JOB", w + 1, work, "SMALL")

    print("TOTAL", total)
    print("BIG", big)

main()
