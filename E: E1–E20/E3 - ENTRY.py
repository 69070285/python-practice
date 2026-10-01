"""E3 - ENTRY"""

def main():
    """Main Function"""
    amount = int(input())
    gold = 0

    for _ in range(amount):
        name, come = input().split()
        if int(come) >= 30:
            print(f"{name} GOLD")
            gold += 1
        elif int(come) >= 15:
            print(f"{name} SILVER")
        elif int(come) >= 5:
            print(f"{name} BRONZE")
        else:
            print(f"{name} NONE")

    print(f"GOLD {gold}")

main()
