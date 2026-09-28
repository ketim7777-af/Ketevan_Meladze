try:
    password = input("Enter your password: ")
    if len (password) < 6:
        raise ValueError("Password is too short.")

except ValueError as e:
    print(e)
    

