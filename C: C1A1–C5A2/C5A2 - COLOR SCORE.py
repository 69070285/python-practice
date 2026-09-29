"""C5A2 - COLOR SCORE"""

def main():
    """Main Function"""
    race = input().split()
    cheer = input().split()
    red = int(race[0]) + int(cheer[0])
    green = int(race[1]) + int(cheer[1])
    blue = int(race[2]) + int(cheer[2])
    yellow = int(race[3]) + int(cheer[3])

    print("RED", red)
    print("GREEN", green)
    print("BLUE", blue)
    print("YELLOW", yellow)
    if red >= green and red >= blue and red >= yellow:
        print("CHAMPION RED")
    elif green >= red and green >= blue and green >= yellow:
        print("CHAMPION GREEN")
    elif blue >= red and blue >= green and blue >= yellow:
        print("CHAMPION BLUE")
    else:
        print("CHAMPION YELLOW")

main()
