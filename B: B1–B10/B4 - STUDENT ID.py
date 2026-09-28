"""B4 - STUDENT ID"""

def main():
    """Main Function"""
    st_id = input()
    year = input()

    if st_id[2:4] != "07":
        print("NOT IT")
    elif int(year[2:]) - int(st_id[:2]) < 0:
        print("TIME TRAVELER")
    else:
        print(f"YEAR {int(year[2:]) - int(st_id[:2]) + 1}")

main()
