"""A5 - ELEVATOR PANEL"""

def main():
    """Main Function"""
    floor = int(input())
    basement = int(input())
    button = 1

    for f in range(1, floor + 1):
        if "4" not in str(f) and f != 13:
            button += 1

    print(f"{button + basement} BUTTONS")
    for f in range(floor, 0, -1):
        if "4" not in str(f) and f != 13:
            print(f)
    print("G")
    for b in range(1, basement + 1):
        print(f"B{b}")

main()
