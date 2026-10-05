"""E6 - ESCAPE"""

def main():
    """Main Function"""
    first = "NOBODY"
    checked = 0

    for _ in range(int(input())):
        name, tall = input().split()
        checked += 1
        if int(tall) >= 140:
            first = name
            break

    print(f"FIRST {first}")
    print(f"CHECKED {checked}")

main()
