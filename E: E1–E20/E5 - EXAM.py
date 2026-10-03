"""E5 - EXAM"""

def main():
    """Main Function"""
    students = int(input())
    passed = 0

    for index in range(1, students + 1):
        name, point = input().split()
        if int(point) >= 50:
            passed += 1
            print(f"{index} {name} PASS")
        else:
            print(f"{index} {name} FAIL")

    print(f"PASSED {passed}")

main()
