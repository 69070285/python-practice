"""D1 - DECK"""

def main():
    """Main Function"""
    amount = int(input())
    people = []

    for _ in range(amount):
        cmd = input().split()
        if cmd[0] == "IN":
            people.append(cmd[1])
        else:
            print("OUT", "NOBODY" if not people else people.pop(0))

    print("WAITING", len(people))
    print(*("-" if not people else people))

main()
