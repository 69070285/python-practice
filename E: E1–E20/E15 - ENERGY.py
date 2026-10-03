"""E15 - ENERGY"""

def main():
    """Main Function"""
    unitList = [int(u) for u in input().split()]
    totalEnergy, highCount = 0, 0

    for i, unit in enumerate(unitList):
        totalEnergy += unit
        if unit > 500:
            highCount += 1
            print(f"UNIT {i + 1} {unit} HIGH")
        else:
            print(f"UNIT {i + 1} {unit} NORMAL")

    print(f"TOTAL {totalEnergy}")
    print(f"HIGH {highCount}")

main()
