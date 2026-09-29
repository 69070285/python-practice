"""B9 - LAB ROWS"""

def main():
    """Main Function"""
    students = int(input())
    per_row = int(input())
    if not students:
        print("EMPTY")
        return
    row = students // per_row
    students %= per_row
    if not students:
        last = per_row
    else:
        row += 1
        last = students

    print(f"ROWS {row}")
    print(f"LAST {last}")

main()
