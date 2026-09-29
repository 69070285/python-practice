"""B8 - KMITL EMAIL"""

def main():
    """Main Function"""
    user = input().lower().split()

    if user[0].isnumeric():
        print(f"{user[0]}@kmitl.ac.th")
    else:
        print(f"{user[0]}.{user[1][:2]}@it.kmitl.ac.th")

main()
