"""A19 - TWO COUNTERS"""

def bigger(left, right):
    """Return Bigger Value"""
    if left > right:
        return left
    return right

def main():
    """Main Function"""
    customers = int(input())
    free_one = free_two = served_one = served_two = total_wait = longest = last_done = 0

    for _ in range(customers):
        arrive, duration = [int(i) for i in input().split()]

        if free_one <= free_two:
            start = arrive if arrive > free_one else free_one
            free_one = start + duration
            served_one += 1
        else:
            start = arrive if arrive > free_two else free_two
            free_two = start + duration
            served_two += 1

        wait = start - arrive
        total_wait += wait
        longest = bigger(longest, wait)
        last_done = start + duration

    print(f"TOTAL WAIT {total_wait}")
    print(f"LONGEST WAIT {longest}")
    print(f"C1 {served_one} C2 {served_two}")
    print(f"CLOSE {last_done}")

main()
