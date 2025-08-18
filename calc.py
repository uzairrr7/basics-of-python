import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,  # real division
    "//": operator.floordiv,
    "%": operator.mod,
    "**": operator.pow
}

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Simple Calculator")
    print("Available operators:", " ".join(ops.keys()))
    while True:
        a = get_number("Enter first number: ")
        op = input("Enter operator (+, -, *, /, //, %, **): ").strip()
        b = get_number("Enter second number: ")

        if op not in ops:
            print("Unknown operator. Try again.")
        else:
            try:
                result = ops[op](a, b)
                print(f"Result: {a} {op} {b} = {result}")
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")

        again = input("Do another? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
