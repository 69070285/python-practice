"""C3A1 - LEAGUE POINTS"""

def main():
    """Main Function"""
    amount = int(input())
    win, draw, lose, ali, enm = 0, 0, 0, 0, 0

    for _ in range(amount):
        b, r = input().split()
        ali += int(b)
        enm += int(r)
        if int(b) > int(r):
            win += 1
        elif int(b) < int(r):
            lose += 1
        else:
            draw += 1

    print(f"W {win} D {draw} L {lose}")
    print(f"POINTS {win * 3 + draw}")
    print(f"GD {ali - enm}")

main()
