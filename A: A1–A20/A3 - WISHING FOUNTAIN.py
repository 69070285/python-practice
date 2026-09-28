"""A3 - WISHING FOUNTAIN"""

def main():
    """Main Function"""
    money = int(input())
    time = int(input())
    people = int(input())

    if money == 1:
        print("REJECTED")
    elif money >= 5 and (time >= 20 or time <= 5) and not people:
        print("GRANTED")
    elif money >= 5 and (time >= 20 or time <= 5) and people:
        print("LEAKED")
    else:
        print("SPLASH")

main()
