"""F1 - SEEDLING"""

def main():
    """Main Function"""
    amount = int(input())
    sapling = input().split()

    print(f"COUNT {amount}")
    print(f"TOP {sapling[0]}")
    print(f"BOTTOM {sapling[-1]}")
    print(f"ORDER {" ".join(sapling[::-1])}")
    print(f"EMPTY {sapling.count("0")}")

main()
