"""G3 - QUEUE"""

def main():
    """Main Function"""
    data = sorted([input().split() for _ in range(int(input()))], key=lambda d: (int(d[1]), d[0]))
    wait, current, name = 0, 0, []

    for d in data:
        wait += current
        current += int(d[1])
        name.append(d[0])

    print("ORDER", *name)
    print("WAIT", wait)

main()
