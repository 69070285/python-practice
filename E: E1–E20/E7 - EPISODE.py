"""E7 - EPISODE"""

def main():
    """Main Function"""
    text = input()
    longest = 0

    for i in text.split("N"):
        if len(i) > longest:
            longest = len(i)

    print("LONGEST", longest)
    print("TOTAL", text.count("Y"))

main()
