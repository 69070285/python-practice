"""G18 - FILMFEST"""

def main():
    """Main Function"""
    shows = []
    plan = []
    free = 0

    for _ in range(int(input())):
        name, start, end = input().split()
        shows.append((name, int(start), int(end)))
    shows.sort(key=lambda show: (show[2], show[1], show[0]))

    for show in shows:
        if show[1] >= free:
            plan.append(show[0])
            free = show[2]

    print(f"SEEN {len(plan)}")
    print("WATCH " + " ".join(plan))

main()
