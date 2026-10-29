def phone_Serch():
    phonebook = {
    "Keti": "577400380"
}

    phonebook["Nino"] = "555123456"
    phonebook["Gio"] = "555234567"
    phonebook["Ana"] = "555345678"

    name = input("Enter name: ")
    print(phonebook.get(name, "Not found"))

phone_Serch()

