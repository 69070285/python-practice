"""C3A2 - TOP SCORER"""

def main():
    """Main Function"""
    amount = int(input())
    score = input().split()
    team, top_score, top_person, zero = 0, -2e9, "", []

    for i in range(amount):
        if int(score[i]) > top_score:
            top_score = int(score[i])
            top_person = i + 1
        if not int(score[i]):
            zero.append(i + 1)
        team += int(score[i])

    print("TEAM", team)
    print("TOP", top_person, top_score)
    print("ZERO", *(zero if zero else ["NONE"]))

main()
