
def require_role(allowed_role="admin"):
    def decorator(func):
        def wrapper(*args, user_role, **kwargs):
            if user_role == allowed_role:
                return func(*args, **kwargs)
            else: 
                print("Permission Denied: User is not an admin.")
           
        return wrapper

    return decorator


@require_role()
def calculate():
    return 3 + 7

result = calculate(user_role="admin")
print(result)



