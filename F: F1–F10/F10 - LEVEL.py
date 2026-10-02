"""F10 - LEVEL"""

def main():
    """Main Function"""
    _ = int(input())
    score = [int(s) for s in input().split()]
    p_score, f_score, grade = [], [], []

    for s in score:
        if s >= 50:
            p_score.append(s)
        else:
            f_score.append(s)
        grade.append(s + 5)

    print("PASS", *(["NONE"] if not p_score else p_score))
    print("FAIL", *(["NONE"] if not f_score else f_score))
    print("GRADE", *grade)
    print("COUNT", len(p_score), len(f_score))

main()
