"""G6 - TIMETABLE"""

def main():
    """Main Function"""
    event = [[n, int(s), int(e)] for _ in range(int(input())) for n, s, e in [input().split()]]
    event.sort(key=lambda e: (e[2], e[1], e[0]))
    current, plan = 0, []

    for n, s, e in event:
        if s >= current:
            plan.append(n)
            current = e

    print("COUNT", len(plan))
    print("PLAN", *plan)

main()
