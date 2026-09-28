"""B3 - PRINT SHOP"""

def main():
    """Main Function"""
    page = int(input())
    color = input()
    card = input()
    if color == "Y":
        price = page * 5
    else:
        price = page

    print(f"SHEETS {(page + 1) // 2}")
    if page >= 50:
        price *= 0.9
    if card == "Y":
        price -= 5
    print("TOTAL 0.00" if price <= 0 else f"TOTAL {price:.2f}")

main()
