"""E1 - ENROLL"""

def main():
    """Main Function"""
    units = int(input())
    extra = 0
    if units > 22:
        extra = 2000
    tuition = units * 800

    print(f"TUITION {tuition}")
    print("FEE 4000")
    print(f"EXTRA {extra}")
    print(f"TOTAL {tuition + 4000 + extra}")

main()
