"""D8 - DETECTOR"""

def main():
    """Main Function"""
    amount = int(input())
    error = 0

    for n in range(amount):
        frame = input()
        if not frame.count("1") % 2:
            print(f"FRAME {n + 1} OK")
        else:
            print(f"FRAME {n + 1} ERROR")
            error += 1

    print(f"ERRORS {error}")

main()
