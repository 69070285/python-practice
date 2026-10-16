"""A9 - FOOD COURT"""

def main():
    """Main Function"""
    seat, minute = input().split()
    seat, minute = int(seat), int(minute)
    current, lost, peak, peak_min = 0, 0, -2e9, -2e9

    for m in range(minute):
        out, come = input().split()
        out, come = int(out), int(come)
        current -= out
        if seat - current >= come:
            current += come
        else:
            lost += current + come - seat
            current = seat
        if current > peak:
            peak = current
            peak_min = m + 1

    print(f"PEAK {peak} AT MINUTE {peak_min}")
    print(f"LOST {lost}")
    print(f"FINAL {current}")

main()
