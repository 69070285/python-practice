"""F2 - WALL"""

def main():
    """Main Function"""
    block = int(input())
    wall = input()
    raw = input().split()
    start, stop = int(raw[0]), int(raw[1])
    if int(raw[0]) > int(raw[1]):
        start, stop = int(raw[1]), int(raw[0])
    result = ""
    paint = 0

    for b in range(block):
        if start <= b + 1 <= stop and wall[b] == ".":
            result += "#"
            paint += 1
        else:
            result += wall[b]

    print("PAINT", paint)
    print(f"LEFT {result.count(".")}")
    print("WALL", result)

main()
