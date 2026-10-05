"""E16 - EXTRACT"""

def main():
    """Main Function"""
    good = 0

    for _ in range(int(input())):
        code = input()
        if len(code) == 6 and code[0].isupper() and code[1:].isnumeric():
            good += 1
            print(code, "GOOD")
        else:
            print(code, "BAD")

    print("GOOD", good)

main()
