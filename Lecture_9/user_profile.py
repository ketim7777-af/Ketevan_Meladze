def create_user_profile(first_name, last_name, role="student", is_active=True):
  
    return {
        "first_name": first_name,
        "last_name": last_name,
        "role": role,
        'is_active': is_active
    }

first_name = input("Enter your first name: ").capitalize()   
last_name = input("Enter your last name: ").capitalize()   

result = create_user_profile(first_name, last_name)
print(result)
      
   