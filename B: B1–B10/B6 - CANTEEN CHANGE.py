"""B6 - CANTEEN CHANGE"""

def main():
    """Main Function"""
    price = int(input())
    paid = int(input())
    change = paid - price
    if change < 0:
        print(f"NOT ENOUGH {abs(change)}")
        return

    print(f"CHANGE {change}")
    print(f"20 {change // 20}")
    change %= 20
    print(f"10 {change // 10}")
    change %= 10
    print(f"5 {change // 5}")
    change %= 5
    print(f"1 {change}")

main()
