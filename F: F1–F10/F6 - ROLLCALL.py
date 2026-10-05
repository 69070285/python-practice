"""F6 - ROLLCALL"""

def main():
    """Main Function"""
    _ = input()
    students = input().split()
    present, extra = 0, []

    for student in input().split():
        if student in students:
            present += 1
            students.remove(student)
        else:
            extra.append(student)

    print("PRESENT", present)
    print("ABSENT", *(students if students else ["NONE"]))
    print("EXTRA", *(extra if extra else ["NONE"]))

main()
