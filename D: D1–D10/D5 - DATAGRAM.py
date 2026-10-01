"""D5 - DATAGRAM"""

def main():
    """Main Function"""
    raw = input().split()
    data, storage = int(raw[0]), int(raw[1])
    pack = data // storage + 1
    last = data % storage
    if not last:
        last = storage
        pack = data // storage

    print(f"PACKETS {pack}")
    print(f"LAST {last}")
    print(f"PADDING {storage - last}")

main()
