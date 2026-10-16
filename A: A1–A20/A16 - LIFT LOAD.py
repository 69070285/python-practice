"""A16 - LIFT LOAD"""

def label(floor):
    """Floor Label"""
    if not floor:
        return "G"
    if floor < 0:
        return f"B{-floor}"
    return f"{floor}"

def move(floor, step, top, base):
    """Lift Move"""
    target = floor + step
    if target > top or target < -base:
        return floor
    return target

def bigger(left, right):
    """Return Bigger Value"""
    if left > right:
        return left
    return right

def main():
    """Main Function"""
    top, base, cap = (int(word) for word in input().split())
    floor, load, heaviest, beep, bonk, work = 0, 0, 0, 0, 0, 0
    line = input().strip()

    while line != "END":
        if line in ("U", "D"):
            new_floor = move(floor, 1 if line == "U" else -1, top, base)
            work += load if new_floor != floor else 0
            if new_floor == floor:
                bonk += 1
            floor = new_floor
        else:
            word, raw_weight = line.split()
            weight = int(raw_weight)
            if word == "OUT":
                load -= weight if load >= weight else load
            elif load + weight > cap:
                beep += 1
            else:
                load += weight
                heaviest = bigger(heaviest, load)
        line = input().strip()

    print(f"END {label(floor)}")
    print(f"LOAD {load}")
    print(f"HEAVIEST {heaviest}")
    print(f"WORK {work}")
    print(f"BEEP {beep}")
    print(f"BONK {bonk}")

main()
