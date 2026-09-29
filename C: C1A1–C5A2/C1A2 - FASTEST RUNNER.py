"""C1A2 - FASTEST RUNNER"""

def main():
    """Main Function"""
    time = [float(t) for t in input().split()]
    fastest = 2e9
    slowest = -2e9

    for t in time:
        if t < fastest:
            fastest = t
        if t > slowest:
            slowest = t

    print(f"FASTEST LANE {time.index(fastest) + 1} TIME {fastest:.2f}")
    print(f"SLOWEST LANE {time.index(slowest) + 1} TIME {slowest:.2f}")
    print(f"GAP {slowest - fastest:.2f}")

main()
