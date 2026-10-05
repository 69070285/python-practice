"""D4 - DUPLICATE"""

def main():
    """Main Function"""
    code = [input() for _ in range(int(input()))]
    used = []
    total = 0

    for c in code:
        if code.count(c) > 1 and c not in used:
            print("DUP", c, code.count(c))
            used.append(c)
            total += code.count(c)

    print("UNIQUE", len(code) - total)

main()
