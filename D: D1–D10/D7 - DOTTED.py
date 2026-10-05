"""D7 - DOTTED"""

def main():
    """Main Function"""
    bad = 0

    for _ in range(int(input())):
        ip = input().split(".")
        if len(ip) == 4 and all(i.isnumeric() for i in ip) and all(0 <= int(i) <= 255 for i in ip):
            if (ip[0] == "10") or (ip[0] == "172" and 16 <= int(ip[1]) <= 31) or\
            (ip[0] == "192" and ip[1] == "168"):
                print(".".join(ip), "OK PRIVATE")
            else:
                print(".".join(ip), "OK PUBLIC")
        else:
            bad += 1
            print(".".join(ip), "BAD")

    print("BAD", bad)

main()
