"""A17 - LOCKER CODE"""

ALPHABET = "SHOPMAL"

def decode(code):
    """Decode Function"""
    if len(code) < 2:
        return -1
    if code[0] == "S" and code != "SS":
        return -1

    value = 0
    digit_sum = 0

    for index in range(len(code) - 1):
        digit = ALPHABET.find(code[index])
        if digit < 0:
            return -1
        value = value * 7 + digit
        digit_sum += digit

    check_index = digit_sum % 7
    expected_check_char = ALPHABET[check_index]
    actual_check_char = code[len(code) - 1]

    if actual_check_char != expected_check_char:
        return -1
    return value

def main():
    """Main Function"""
    valid = 0
    total = 0
    line = input().strip()
    while line != "END":
        number = decode(line)
        if number < 0:
            print("INVALID")
        else:
            print(number)
            valid += 1
            total += number
        line = input().strip()
    print(f"VALID {valid} SUM {total}")

main()
