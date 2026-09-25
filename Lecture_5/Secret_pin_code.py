#  ვარიანტი N1 (ეს ჯობია ალბათ)

tries = 0

while True:
    password = input("Enter a 4-digit PIN code: ")
    if password == "1234" and tries < 3:
        print("Access granted!")
        break
    print (f"Incorrect PIN. Remaining attampts {3 - (tries + 1)}.")
    tries += 1

    if tries == 3:
        print("Card blocked!")
        break


#  ვარიანტი N2

password = ""
tries = 0


while password != "1234" and tries < 3:
    password = input("Enter a 4-digit PIN code: ")
    tries += 1
    

    if password != "1234" and tries < 3:
        print(f"Incorrect PIN. Remaining attampts {3 - (tries)} ")
    elif password != "1234" and tries == 3:
        print(f"Incorrect PIN. Remaining attampts {3 - (tries)}. Card blocked!")
    else:
        print("Access granted")
        break