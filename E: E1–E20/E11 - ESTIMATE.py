"""E11 - ESTIMATE"""

def main():
    """Main Function"""
    amount = int(input())
    total = 0

    for n in range(amount):
        unit = int(input())
        price = unit * 8
        if unit > 150:
            price += 200
        total += price
        print(f"ROOM {n + 1} {price}")

    print(f"TOTAL {total}")

main()
