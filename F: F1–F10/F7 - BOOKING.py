"""F7 - BOOKING"""

def main():
    """Main Function"""
    amount, people = input().split()
    period = [0] * int(amount)
    busy = 0

    for _ in range(int(people)):
        start, stop = input().split()
        for t in range(int(start), int(stop) + 1):
            period[t - 1] += 1

    for i in period:
        if i > busy:
            busy = i

    print("SLOT", *period)
    print("BUSY", period.index(busy) + 1, busy)

main()
