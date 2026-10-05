"""D3 - DRAWER"""

def main():
    """Main Function"""
    _ = int(input())
    drawer = input().split()

    for _ in range(int(input())):
        want = input()
        if want in drawer:
            print(f"FOUND {want} AT {drawer.index(want) + 1}")
        else:
            print("MISSING", want)

    print("EMPTY", drawer.count("0"))

main()
