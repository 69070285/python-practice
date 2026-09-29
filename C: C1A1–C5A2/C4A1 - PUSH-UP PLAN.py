"""C4A1 - PUSH-UP PLAN"""

def main():
    """Main Function"""
    start = int(input())
    step = int(input())
    target = int(input())
    day, total = 0, 0

    while start - step < target:
        day += 1
        total += start
        print(f"DAY {day} {start}")
        start += step

    print(f"TARGET REACHED ON DAY {day}")
    print(f"TOTAL {total}")

main()
