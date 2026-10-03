"""E17 - EVALUATE"""

def main():
    """Main Function"""
    tech, office, other = 0, 0, 0

    for _ in range(int(input())):
        name, code = input().split()
        if code in ("IT", "DEV", "OPS"):
            tech += 1
            print(name, "TECH")
        elif code in ("HR", "FIN", "ADM"):
            office += 1
            print(name, "OFFICE")
        else:
            other += 1
            print(name, "OTHER")

    print(f"TECH {tech}")
    print(f"OFFICE {office}")
    print(f"OTHER {other}")

main()
