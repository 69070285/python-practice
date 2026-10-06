"""E19 - ENSEMBLE"""

def main():
    """Main Function"""
    amount = int(input())
    tone, rhythm, show, passed, failed, total = 0, 0, 0, 0, 0, 0

    for n in range(amount):
        t, r, s = [int(i) for i in input().split()]
        tone += t
        rhythm += r
        show += s
        add = t + r + s
        total += add
        if add >= 21:
            passed += 1
            print(f"BAND {n + 1} {add} PASS")
        else:
            failed += 1
            print(f"BAND {n + 1} {add} FAIL")

    print("TONE", tone)
    print("RHYTHM", rhythm)
    print("SHOW", show)
    print("PASSED", passed)
    print("FAILED", failed)
    print(f"AVERAGE {total / amount:.2f}")

main()
