"""A10 - BOX PYRAMID"""

def main():
    """Main Function"""
    n = int(input())

    for i in range(1, n + 1):
        spaces = " " * (2 * (n - i))
        print(spaces + "+---" * i + "+")
        print(spaces + "|   " * i + "|")
    print("+---" * n + "+")

main()
