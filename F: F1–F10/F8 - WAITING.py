"""F8 - WAITING"""

def main():
    """Main Function"""
    amount, target = input().split()
    fast, slow, over = 2e9, -2e9, 0
    fast_person, slow_person = "", ""

    for _ in range(int(amount)):
        name, wait = input().split()
        if int(wait) < fast:
            fast = int(wait)
            fast_person = name
        if int(wait) > slow:
            slow = int(wait)
            slow_person = name
        if int(wait) > int(target):
            over += 1

    print("FAST", fast_person, fast)
    print("SLOW", slow_person, slow)
    print("OVER", over)

main()
