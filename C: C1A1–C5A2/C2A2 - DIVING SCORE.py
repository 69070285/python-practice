"""C2A2 - DIVING SCORE"""

def main():
    """Main Function"""
    action = float(input())
    score = [float(s) for s in input().split()]
    total = 0
    least = 2e9

    for s in score:
        if s < least:
            least = s
    score.remove(least)
    for s in score:
        total += s

    print(f"DROP {least:.1f}")
    print(f"SCORE {(total / len(score)) * action:.2f}")

main()
