"""G19 - LUNCHBOX"""

def main():
    """Main Function"""
    head = input().split()
    space = int(head[1])
    total, taken, boxes = 0, [], []

    for _ in range(int(head[0])):
        name, grams, price = input().split()
        boxes.append((name, int(grams), int(price)))

    boxes.sort(key=lambda box: (-box[2] // box[1], box[0]))

    for box in boxes:
        if not space:
            break
        scoop = min(box[1], space)
        total += (box[2] // box[1]) * scoop
        space -= scoop
        taken.append(f"{box[0]}:{scoop}")

    print(f"VALUE {total}")
    print("TAKE " + (" ".join(taken) or "NONE"))

main()
