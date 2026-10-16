"""G11 - CABLE"""

def main():
    """Main Function"""
    n, cables = int(input()), [int(c) for c in input().split()]
    cost, joins = 0, []
    if n == 1:
        print("COST 0\nJOIN NONE")
        return

    while len(cables) > 1:
        cables.sort()
        a, b = cables.pop(0), cables.pop(0)
        joins.append(f"{a}+{b}")
        cost += a + b
        cables.append(a + b)

    print(f"COST {cost}\nJOIN {' '.join(joins)}")

main()
