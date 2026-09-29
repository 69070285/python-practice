"""C2A1 - SWIM LAPS"""

def main():
    """Main Function"""
    step = int(input())
    stop = int(input())
    start = 0
    lap = 0

    while start < stop:
        lap += 1
        start += step
        print(f"LAP {lap} {start}")

    print(f"DONE IN {lap} LAPS")
    print(f"EXTRA {start - stop}")

main()
