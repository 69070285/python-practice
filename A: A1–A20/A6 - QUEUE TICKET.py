"""A6 - QUEUE TICKET"""

def main():
    """Main Function"""
    fast = 0
    normal = 0

    while True:
        data = input()

        if data == "CLOSE":
            break
        if 12 < int(data) < 60:
            normal += 1
            print(f"N{normal:03d}")
        else:
            fast += 1
            print(f"F{fast:03d}")

    print(f"F {fast} N {normal}")

main()
