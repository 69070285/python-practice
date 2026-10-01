"""E12 - EXPENSE"""

def main():
    """Main Function"""
    amount = int(input())
    total = 0

    for _ in range(amount):
        item, price, qty = input().split()
        price, qty = int(price), int(qty)
        pay = price * qty
        total += pay
        print(f"{item} {qty} x {price} = {pay}")

    print(f"GRAND {total}")

main()
