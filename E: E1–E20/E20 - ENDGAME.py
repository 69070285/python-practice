"""E20 - ENDGAME"""

def main():
    """Main Function"""
    amount = int(input())
    hit = ("PADTHAI", "TOMYUM", "SOMTAM")
    big, total = 0, 0

    for i in range(amount):
        food, price, qty = input().split()
        pay = int(price) * int(qty)
        total += pay
        if pay >= 300:
            big += 1
            print(f"ORDER {i + 1} {food} {pay} {"BIG HIT" if food in hit else "BIG"}")
        else:
            print(f"ORDER {i + 1} {food} {pay} {"SMALL HIT" if food in hit else "SMALL"}")

    print("TOTAL", total)
    print("BIG", big)
    print(f"AVERAGE {total / amount:.2f}")

main()
