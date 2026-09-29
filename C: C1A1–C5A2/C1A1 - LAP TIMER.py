"""C1A1 - LAP TIMER"""

def main():
    """Main Function"""
    lap = int(input())
    total = 0

    for l in range(1, lap + 1):
        time = int(input())
        print(f"LAP {l} {time} SLOW" if time > 60 else f"LAP {l} {time}")
        total += time

    print(f"TOTAL {total}")
    print(f"AVERAGE {total / lap:.2f}")

main()
