"""D6 - DOWNLINK"""

def main():
    """Main Function"""
    amount = int(input())
    total = 0

    for i in range(amount):
        data = input().split()
        work, speed = int(data[0]), int(data[1])
        method = work / (speed / 8)
        total += method
        if method <= 10:
            print(f"FILE {i + 1} {method:.2f} FAST")
        elif method <= 60:
            print(f"FILE {i + 1} {method:.2f} OK")
        else:
            print(f"FILE {i + 1} {method:.2f} SLOW")

    print(f"TOTAL {total:.2f}")

main()
