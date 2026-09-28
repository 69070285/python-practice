"""A1 - PARKING GATE"""

from math import ceil

def main():
    """Main Function"""
    park_time = int(input())
    access = input()
    if access == "Y":
        limit = 5
    else:
        limit = 3

    if park_time / 60 <= limit:
        print("FREE")
    else:
        print(ceil(park_time / 60 - limit) * 20)

main()
