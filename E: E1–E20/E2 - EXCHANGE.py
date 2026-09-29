"""E2 - EXCHANGE"""

def main():
    """Main Function"""
    total = int(input())
    people = int(input())
    each = total // people
    extra = total % people

    print(f"EACH {each}")
    print(f"EXTRA {extra}")
    print(f"PAYER {each + extra}")

main()
