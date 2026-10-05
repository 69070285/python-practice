"""E8 - EMPTY"""

def main():
    """Main Function"""
    jobs = []

    for _ in range(int(input())):
        order = input().split()
        if order[0] == "ADD":
            jobs.append(order[1])
        elif order[0] == "COUNT":
            print(f"COUNT {len(jobs)}")
        else:
            print(f"DONE {jobs.pop() if jobs else "NONE"}")

    print(f"LEFT {len(jobs)}")

main()
