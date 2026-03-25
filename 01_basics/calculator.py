# calculator.py
# Day 2 - Interactive CLI Calculator (keeps running after errors)

def ask_yes_no(prompt: str) -> bool:
    """
    Returns True for yes, False for no.
    Keeps asking until the user enters a valid answer.
    """
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type 'yes' or 'no' (or y/n).")


print("=== SIMPLE CALCULATOR ===")

while True:
    try:
        num1 = float(input("\nEnter first number: ").strip())
        num2 = float(input("Enter second number: ").strip())

        print("\n--- RESULTS ---")
        print(f"{num1} + {num2} = {num1 + num2}")
        print(f"{num1} - {num2} = {num1 - num2}")
        print(f"{num1} * {num2} = {num1 * num2}")

        # Handle division safely
        if num2 == 0:
            print(f"{num1} / {num2} = ERROR (division by zero)")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")

    except ValueError:
        print("\nERROR: Please enter valid numbers only.")

    # Ask whether to continue (after success OR error)
    if not ask_yes_no("\nDo you want to continue? (yes/no): "):
        print("Goodbye!")
        break