"""B5 - PROJECT ROOM"""

def main():
    """Main Function"""
    people = int(input())
    hour = float(input())
    day = input()
    advisor = input()

    if people < 3:
        print("TOO SMALL")
    elif people > 8:
        print("TOO BIG")
    elif hour > 3:
        print("TOO LONG")
    elif day == "WEEKEND" and advisor == "N":
        print("NEED ADVISOR")
    else:
        print("BOOKED")

main()
