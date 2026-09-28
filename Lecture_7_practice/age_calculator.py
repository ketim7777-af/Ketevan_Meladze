try:
    birth_year = int(input("Enter your birth year:"))
    print("Approximate year:", 2026 - birth_year)

except ValueError:
    print("Please enter only numbers")