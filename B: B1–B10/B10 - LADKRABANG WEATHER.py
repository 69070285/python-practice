"""B10 - LADKRABANG WEATHER"""

def main():
    """Main Function"""
    celsius = float(input())

    print(f"F {celsius * 9 / 5 + 32:.1f}")
    if celsius >= 35:
        print("HOT")
    elif celsius >= 28:
        print("WARM")
    else:
        print("COOL")

main()
