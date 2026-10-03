"""E14 - EXPORT"""

def main():
    """Main Function"""
    days = int(input())
    total = 0

    for number in range(1, days + 1):
        sale = int(input())
        total += sale
        if sale >= 10000:
            print("DAY", number, sale, "OK")
        else:
            print("DAY", number, sale, "LOW")

    print("TOTAL", total)
    print(f"AVERAGE {total / days:.2f}")

main()
