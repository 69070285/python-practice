"""G2 - BASKET"""

def main():
    """Main Function"""
    _, money = map(int, input().split())
    price = sorted(list(map(int, input().split())))
    spent, count, start = 0, 0, money

    for p in price:
        if money >= p:
            money -= p
            spent += p
            count += 1

    print("COUNT", count)
    print("SPENT", spent)
    print("LEFT", start - spent)

main()
