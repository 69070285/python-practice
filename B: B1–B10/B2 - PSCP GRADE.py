"""B2 - PSCP GRADE"""

def main():
    """Main Function"""
    score = float(input())
    lab = input()
    if lab == "Y":
        score += 2
        if score > 100:
            score = 100

    print(f"SCORE {score:.2f}")
    if score >= 80:
        print("GRADE A")
    elif score >= 75:
        print("GRADE B+")
    elif score >= 70:
        print("GRADE B")
    elif score >= 65:
        print("GRADE C+")
    elif score >= 60:
        print("GRADE C")
    elif score >= 55:
        print("GRADE D+")
    elif score >= 50:
        print("GRADE D")
    else:
        print("GRADE F")

main()
