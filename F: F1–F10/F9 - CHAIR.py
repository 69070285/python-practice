"""F9 - CHAIR"""

def main():
    """Main Function"""
    _, event = input().split()
    queue = input().split()

    for _ in range(int(event)):
        cmd = input().split()
        if cmd[0] == "SHOW":
            print("SHOW", *queue)
        elif cmd[0] == "FLIP":
            queue.reverse()
        else:
            queue = queue[int(cmd[1]):] + queue[:int(cmd[1])]

    print("FINAL", *queue)

main()
