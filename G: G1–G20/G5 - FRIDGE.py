"""G5 - FRIDGE"""

def main():
    """Main Function"""
    fridge = [[f, int(d)] for _ in range(int(input())) for f, d in [input().split()]]
    fridge.sort(key=lambda f: (f[1], f[0]))
    eat, waste, day = [], [], 1

    while fridge:
        eat.append(fridge[0][0])
        fridge.pop(0)
        while fridge and fridge[0][1] == day:
            waste.append(fridge[0][0])
            fridge.pop(0)
        day += 1

    print("EAT", len(eat))
    print("ORDER", *eat)
    print("WASTE", *(waste if waste else ["NONE"]))

main()
