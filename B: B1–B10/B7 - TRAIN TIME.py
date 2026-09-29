"""B7 - TRAIN TIME"""

def main():
    """Main Function"""
    start = input().split(":")
    start = int(start[0]) * 60 + int(start[1])
    stop = input().split(":")
    stop = int(stop[0]) * 60 + int(stop[1])
    wait = stop - start

    print(f"{wait // 60 % 24} HOUR {wait % 60} MIN")

main()
