"""E10 - EXACTLY"""

def main():
    """Main Function"""
    best_name = ""
    best_score = -2e9
    best_time = 2e9

    for _ in range(int(input())):
        name, points, seconds = input().split()
        score = int(points)
        clock = int(seconds)
        if (score > best_score) or (score == best_score and clock < best_time):
            best_name = name
            best_score = score
            best_time = clock

    print(f"WINNER {best_name}")
    print(f"SCORE {best_score}")
    print(f"TIME {best_time}")

main()
