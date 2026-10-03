"""G1 - CHANGE"""

def main():
    """Main Function"""
    baht = [1000, 500, 100, 50, 20, 10, 5, 1]
    total = 0

    for _ in range(int(input())):
        change = []
        money = int(input())
        stay = money

        for b in baht:
            calculate = money // b
            money %= b
            if calculate:
                total += calculate
                change.append(f"{b}x{calculate}")

        print(stay, *(["NONE"] if not stay else change))

    print("TOTAL", total)

main()
