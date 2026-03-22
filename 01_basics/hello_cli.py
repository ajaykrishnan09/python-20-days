# hello_cli.py

name = input("Enter your name: ").strip()
age = input("Enter your age: ").strip()

print("\n--- RESULT ---")
print(f"Hello, {name}!")
print(f"In 5 years, you will be {int(age) + 5} years old.")