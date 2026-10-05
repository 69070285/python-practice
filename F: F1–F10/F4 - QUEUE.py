"""F4 - QUEUE"""

def main():
    """Main Function"""
    _, amount = input().split()
    queue = input().split()

    for _ in range(int(amount)):
        order = input().split()
        if order[0] == "ADD":
            queue.append(order[1])
        elif order[0] == "CUT":
            queue.insert(int(order[1]) - 1, order[2])
        elif order[0] == "OUT":
            queue.remove(order[1])
        else:
            print("WHERE", order[1], queue.index(order[1]) + 1 if order[1] in queue else "NONE")

    print("COUNT", len(queue))
    print("QUEUE", *queue)

main()
