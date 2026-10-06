"""G7 - BUFFET"""

def main():
    """Main Function"""
    amount, limit = map(int, input().split())
    buffet = [[f, int(g), int(p)] for _ in range(amount) for f, g, p in [input().split()]]
    buffet.sort(key=lambda b: (-(b[2] // b[1]), b[0]))
    value, take = 0, []

    for f, g, p in buffet:
        if not limit:
            break
        portion = min(limit, g)
        take.append(f"{f}:{portion}")
        value += (p // g) * portion
        limit -= portion

    print("VALUE", value)
    print("TAKE", *(take if take else ["NONE"]))

main()
