"""G8 - CHARGE"""

def main():
    """Main Function"""
    amount, target, duration = map(int, input().split())
    station = sorted(list(map(int, f"{input()} {target}".split())))
    start, charge, i = duration, [], 0

    while start < target:
        furthest = -1
        while i < amount and station[i] <= start:
            furthest = station[i]
            i += 1

        if furthest in (-1, target):
            break

        charge.append(furthest)
        start = furthest + duration

    if start < target:
        print("IMPOSSIBLE")
    else:
        print("STOPS", len(charge))
        print("AT", *(charge if charge else ["NONE"]))

main()
