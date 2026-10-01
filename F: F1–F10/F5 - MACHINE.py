"""F5 - MACHINE"""

def main():
    """Main Function"""
    _ = int(input())
    state = input().split()
    normal, hot, shake, stop = 0, 0, 0, 0

    for s in state:
        if s == "O":
            normal += 1
        elif s == "H":
            hot += 1
        elif s == "V":
            shake += 1
        else:
            stop += 1

    print(f"NORMAL {normal}")
    print(f"HOT {hot}")
    print(f"SHAKE {shake}")
    print(f"STOP {stop}")
    print("FIRST NONE" if not stop else f"FIRST {state.index("S") + 1}")

main()
