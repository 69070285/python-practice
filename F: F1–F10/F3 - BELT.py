"""F3 - BELT"""

def main():
    """Main Function"""
    limit, amount = input().split()
    limit, amount = int(limit), int(amount)
    box = input().split()
    drop, belt = [], []

    for b in range(amount):
        if len(box) - b <= limit:
            belt.append(box[b])
        else:
            drop.append(box[b])

    print("DROP", *(["NONE"] if not drop else drop))
    print("BELT", *belt)
    print("LEFT", len(belt))

main()
