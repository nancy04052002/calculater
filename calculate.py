
"""
Simple command-line calculator supporting +, -, *, /.
Run: python calculator.py
"""

from typing import Callable, Tuple, List


def add(a: float, b: float) -> float:
    """Return a + b"""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a - b"""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return a * b"""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a / b. Raises ZeroDivisionError if b == 0."""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b


OP_MAP = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide),
    "+": ("Add", add),
    "-": ("Subtract", subtract),
    "*": ("Multiply", multiply),
    "/": ("Divide", divide),
}


def get_number(prompt: str) -> float:
    """Prompt the user until a valid float is entered."""
    while True:
        try:
            s = input(prompt).strip()
            if s.lower() in ("q", "quit", "exit"):
                raise KeyboardInterrupt
            return float(s)
        except ValueError:
            print("  → That doesn't look like a valid number. Please try again.")
        except KeyboardInterrupt:
            raise


def get_operation() -> Tuple[str, Callable[[float, float], float]]:
    """Show menu and return (operation_name, function). Keeps asking until valid."""
    menu = """
Choose an operation:
  1) Add (+)
  2) Subtract (-)
  3) Multiply (*)
  4) Divide (/)
  q) Quit
Enter choice (1/2/3/4 or + - * / or q): """
    while True:
        choice = input(menu).strip().lower()
        if choice in ("q", "quit", "exit"):
            raise KeyboardInterrupt
        if choice in OP_MAP:
            name, func = OP_MAP[choice]
            return name, func
        print("  → Invalid choice. Try again.")


def print_history(history: List[str]) -> None:
    if not history:
        print("No calculations yet.")
        return
    print("\nCalculation history:")
    for i, entry in enumerate(history, 1):
        print(f"  {i}. {entry}")
    print()


def main():
    print("Simple CLI Calculator — supports +, -, *, /")
    print("Type 'q' at any prompt to exit.\n")
    history: List[str] = []
    last_result: float | None = None

    try:
        while True:
            try:
                op_name, op_func = get_operation()
            except KeyboardInterrupt:
                print("\nExiting calculator. Goodbye!")
                break

            if last_result is not None:
                use_last = input(f"Use last result ({last_result}) as first number? (y/N): ").strip().lower()
                if use_last == "y":
                    a = last_result
                    print(f"First number = {a}")
                else:
                    try:
                        a = get_number("Enter first number: ")
                    except KeyboardInterrupt:
                        print("\nExiting calculator. Goodbye!")
                        break
            else:
                try:
                    a = get_number("Enter first number: ")
                except KeyboardInterrupt:
                    print("\nExiting calculator. Goodbye!")
                    break

            try:
                b = get_number("Enter second number: ")
            except KeyboardInterrupt:
                print("\nExiting calculator. Goodbye!")
                break

            try:
                result = op_func(a, b)
            except ZeroDivisionError as zde:
                print("  → Error:", zde)
                continue
            except Exception as exc:
                print("  → Unexpected error:", exc)
                continue

            entry = f"{a} {op_name} {b} = {result}"
            history.append(entry)
            last_result = result
            print("\nResult:", result)
            print_history(history)

          
            cont = input("Press Enter to continue, or type 'q' to quit: ").strip().lower()
            if cont in ("q", "quit", "exit"):
                print("Goodbye!")
                break

    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye!")

if __name__ == "__main__":
    main()