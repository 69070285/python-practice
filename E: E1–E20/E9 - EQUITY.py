"""E9 - EQUITY"""

def main():
    """Main Function"""
    submitted = 0
    missing = 0
    total = 0

    for _ in range(int(input())):
        score = int(input())
        if score >= 0:
            submitted += 1
            total += score
        else:
            missing += 1

    print(f"SUBMITTED {submitted}")
    print(f"AVERAGE {f"{total / submitted:.2f}" if submitted else "NONE"}")
    print(f"MISSING {missing}")

main()
