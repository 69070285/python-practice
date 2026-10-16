"""G9 - PLUGS"""

def main():
    """Main Function"""
    time = [[int(n) for n in input().split()] for _ in range(int(input()))]
    time.sort(key=lambda t: t[0])
    since, most = 0, -2e9

    for _, t in enumerate(time):
        count = 0
        for s, e in time:
            if s <= t[0] < e:
                count += 1
        if count > most:
            since = t[0]
            most = count

    print("PLUGS", most)
    print("SINCE", since)

main()
