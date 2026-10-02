"""D1 - DECK"""

def main():
    """Main Function"""
    amount = int(input())
    card = []

    for _ in range(amount):
        cmd = input().split()
        if cmd[0] == "PUT":
            card.append(cmd[1])
        else:
            print("TAKE", "EMPTY" if not card else card.pop())

    print("LEFT", len(card))
    print("TOP", "EMPTY" if not card else card[-1])

main()
