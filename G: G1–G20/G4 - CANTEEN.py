"""G4 - CANTEEN"""

def main():
    """Main Function"""
    amount, choose = map(int, input().split())
    menu = [[n, g, int(s)] for _ in range(amount) for n, g, s in [input().split()]]
    menu.sort(key=lambda m: (-m[2], m[0]))
    pick, used, total = [], [], 0

    for name, group, score in menu:
        if group not in used and choose:
            pick.append(name)
            used.append(group)
            total += score
            choose -= 1

    print("PICK", *pick)
    print("SCORE", total)

main()
