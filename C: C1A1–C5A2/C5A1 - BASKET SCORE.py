"""C5A1 - BASKET SCORE"""

def main():
    """Main Function"""
    amount = int(input())
    red, blue = 0, 0

    for _ in range(amount):
        result = input().split()
        if result[0] == "R":
            red += int(result[1])
        else:
            blue += int(result[1])

    print(f"RED {red}")
    print(f"BLUE {blue}")
    if red > blue:
        print("WINNER RED")
    elif red < blue:
        print("WINNER BLUE")
    else:
        print("DRAW")

main()
