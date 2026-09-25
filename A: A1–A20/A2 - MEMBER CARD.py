"""A2 - MEMBER CARD"""

def main():
    """Main Function"""
    spend = int(input())
    exp = int(input())
    if spend < 10000:
        member = 1
    elif 10000 <= spend < 50000:
        member = 2
    elif 50000 <= spend < 200000:
        member = 3
    elif 200000 <= spend < 1000000:
        member = 4
    else:
        member = 5

    if exp >= 10:
        member += 1

    if member == 1:
        print("Paper")
    elif member == 2:
        print("Bronze")
    elif member == 3:
        print("Silver")
    elif member == 4:
        print("Gold")
    else:
        print("Mythril")

main()
