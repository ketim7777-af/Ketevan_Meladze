class User:

    status = "Active"
    
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def get_info(self):
    
        print(f"Status: {self.status}")
        print(f"User name: {self.username}")
        print(f"E-mail: {self.email}")
        print(f"Age: {self.age}")

user_1 = User("Ketim7777", "ketim7777@gmail.com", "49")
user_1.get_info()

print("=" *30)

user_2 = User("Saba2005", "Sava@gmail.com", "21")
user_2.get_info()

print("=" *30)

print(f"User_1 status: {user_1.status}")
print(f"User_2 status: {user_2.status}")