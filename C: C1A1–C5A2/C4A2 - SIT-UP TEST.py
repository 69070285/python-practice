"""C4A2 - SIT-UP TEST"""

def main():
    """Main Function"""
    target = int(input())
    sit_up = [int(s) for s in input().split()]
    passed, failed = [], []
    best = -2e9

    for s in sit_up:
        if s > best:
            best = s
        if s >= target:
            passed.append(s)
        else:
            failed.append(s)

    print(f"PASS {passed}")
    print(f"FAIL {failed}")
    print(f"PASSED {len(passed)} OF {len(sit_up)}")
    print(f"BEST {sit_up.index(best) + 1}")

main()
