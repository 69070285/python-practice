"""A11 - TIDY TAGS"""

def main():
    """Main Function"""
    s, e = [int(i) for i in input().split()]
    tidy = highest = 0

    for num in range(s, e + 1):
        n, last, ok = num, 10, True
        while n and ok:
            n, curr = divmod(n, 10)
            if curr >= last:
                ok = False
                break
            last = curr
        if ok:
            tidy, highest = tidy + 1, num

    print(f"TIDY {tidy}\nMAX {highest or 'NONE'}")

main()
