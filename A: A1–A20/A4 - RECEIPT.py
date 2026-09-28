"""A4 - RECEIPT"""

def main():
    """Main Function"""
    amount = int(input())
    total = 0

    for _ in range(amount):
        item = input().split()
        price, qty = int(item[0]), int(item[1])
        total += price * qty

    if total >= 1000:
        print(f"PAY {total * 0.9:.2f}")
    elif total < 0:
        print(f"THEY PAY YOU {abs(total)}")
    else:
        print(f"PAY {total:.2f}")

main()
