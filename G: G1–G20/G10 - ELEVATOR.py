"""G10 - ELEVATOR"""

def main():
    """Main Function"""
    head = input().split()
    cap = int(head[1])
    boxes = sorted(int(x) for x in input().split())
    light, heavy = 0, len(boxes) - 1
    trips, pairs = 0, 0

    while light <= heavy:
        if light < heavy and boxes[light] + boxes[heavy] <= cap:
            heavy -= 1
            pairs += 1
        heavy -= 1
        trips += 1

    print(f"TRIPS {trips}")
    print(f"PAIRS {pairs}")

main()
