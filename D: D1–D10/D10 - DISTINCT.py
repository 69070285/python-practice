"""D10 - DISTINCT"""

def main():
    """Main Function"""
    a = input().split()
    b = input().split()

    inter = [n for n in a if n in b]
    only_a = [n for n in a if n not in b]
    union = a + [n for n in b if n not in a]

    print("UNION", *union)
    print("INTER", *("-" if not inter else inter))
    print("ONLYA", *("-" if not only_a else only_a))

main()
