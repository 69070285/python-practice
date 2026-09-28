"""B1 - BUILDING HOURS"""

def main():
    """Main Function"""
    day = input()
    time = input().split(":")
    hour = int(time[0])

    if (day in "MON TUE WED THU FRI" and 7 <= hour < 22) or (day in "SAT SUN" and 9 <= hour < 17):
        print("OPEN")
    else:
        print("CLOSED")

main()
