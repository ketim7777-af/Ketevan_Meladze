try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError ("Age can not be negative")
    elif age < 18:
        raise ValueError ("For registration you must be at least 18 years old")

except ValueError as e:
    print(e)

finally:
    print("Registration process is finished")

    