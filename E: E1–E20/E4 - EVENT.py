"""E4 - EVENT"""

def main():
    """Main Function"""
    booths = int(input())
    total,reached = 0, 0

    for _ in range(booths):
        sale = int(input())
        total += sale
        if sale >= 5000:
            reached += 1

    print("TOTAL", total)
    print("REACHED", reached)
    print(f"AVERAGE {total / booths:.2f}")

main()
