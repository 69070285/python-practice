"""A7 - FLASH SALE"""

def main():
    """Main Function"""
    price = int(input())
    promo = int(input())
    target = int(input())
    hour = 0

    while price > target:
        discount = price * promo // 100
        if not discount:
            print("NEVER")
            return
        price -= discount
        hour += 1

    print(f"BUY AT HOUR {hour} PRICE {price}")

main()
