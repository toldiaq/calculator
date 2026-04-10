def main(input_str: str) -> str:
    parts = input_str.strip().split()

    if len(parts) != 3:
        raise Exception("throws Exception")

    try:
        a = int(parts[0])
        b = int(parts[2])
    except ValueError:
        raise Exception("throws Exception")

    op = parts[1]

    if a < 1 or a > 10 or b < 1 or b > 10:
        raise Exception("throws Exception")

    if op == "+":
        return str(a + b)
    elif op == "-":
        return str(a - b)
    elif op == "*":
        return str(a * b)
    elif op == "/":
        return str(a // b)
    else:
        raise Exception("throws Exception")

if __name__ == "__main__":
    try:
        user_input = input()
        print(main(user_input))
    except Exception as e:
        print(e)