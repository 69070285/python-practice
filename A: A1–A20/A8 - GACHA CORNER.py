"""A8 - GACHA CORNER"""

def main():
    """Main Function"""
    x = int(input())
    a = int(input())
    c = int(input())
    k = int(input())

    for i in range(1, k + 1):
        x = (a * x + c) % 1000
        if not x % 17:
            print(f"RARE AT TURN {i}")
            return

    print(f"BROKE AFTER {k} TURNS")

main()
