"""D9 - DIVISORS"""

def main():
    """Main Function"""
    n1, n2 = input().split()
    n1, n2 = int(n1), int(n2)
    gcd = []

    for check in range(1, n1 + 1):
        if not n1 % check and not n2 % check:
            gcd.append(check)

    print(*gcd)
    print("GCD", gcd[-1])
    print("COPRIME", "YES" if gcd[-1] == 1 else "NO")

main()
