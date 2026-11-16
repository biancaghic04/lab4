#ex 2
# python3 "lab4 ex2.py"


def read_numbers():
    with open("numbers.txt", "r") as file:
        lines = file.readlines()

    if len(lines) != 2:
        raise ValueError("The file must contain exactly two numbers.")

    a = lines[0].strip()
    b = lines[1].strip()

    for number in [a, b]:
        if not number.isdigit() or len(number) > 200:
            raise ValueError("Numbers must have 1 to 200 digits.")

    return a.lstrip("0") or "0", b.lstrip("0") or "0"


def add_numbers(a, b):
    a = a[::-1]
    b = b[::-1]

    result = ""
    carry = 0

    for i in range(max(len(a), len(b))):
        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0

        total = digit_a + digit_b + carry

        result = str(total % 10) + result
        carry = total // 10

    if carry:
        result = str(carry) + result

    return result.lstrip("0") or "0"


def multiply_numbers(a, b):
    if a == "0" or b == "0":
        return "0"

    result = [0] * (len(a) + len(b))

    for i in range(len(a) - 1, -1, -1):
        for j in range(len(b) - 1, -1, -1):
            product = int(a[i]) * int(b[j])
            position = i + j + 1

            total = product + result[position]
            result[position] = total % 10
            result[position - 1] += total // 10

    return "".join(str(digit) for digit in result).lstrip("0") or "0"


def main():
    try:
        a, b = read_numbers()

        print("First number:", a)
        print("Second number:", b)
        print("Sum:", add_numbers(a, b))
        print("Product:", multiply_numbers(a, b))

    except FileNotFoundError:
        print("Error: numere.txt was not found.")

    except ValueError as error:
        print("Error:", error)


main()