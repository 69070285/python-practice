"""E13 - ENGINE"""

def main():
    """Main Function"""
    amount = int(input())
    run, stop = 0, 0

    for n in range(amount):
        state = input()
        if state == "RUN":
            print(f"MACHINE {n + 1} RUN")
            run += 1
        else:
            stop += 1

    print("RUNNING", "NONE" if not run else run)
    print("STOPPED", stop)

main()
