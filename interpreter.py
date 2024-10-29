


def add_number(first_number,last_number,math_number):
    first_number = float(first_number)
    last_number = float(last_number)

    if math_number == '+':
        result = first_number + last_number
    elif math_number == '-':
        result = first_number - last_number
    elif math_number == '*':
        result = first_number * last_number
    elif math_number == '/':
        result = first_number / last_number
    return result


def main():
    name = input("expression: ")

    parts = name.split()
    if len(parts) >= 3:
        first_number = parts[0]
        math_number = parts[1]
        last_number = parts [2]

    result = add_number(first_number,last_number,math_number)
    print(f"{result:.1f}")


if __name__ == "__main__":
    main()
