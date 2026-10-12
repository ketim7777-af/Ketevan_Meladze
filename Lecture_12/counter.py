
def make_counter():
    start_value = 0
    def closure ():
        nonlocal start_value
        start_value +=1
        return start_value

    return closure

counter = make_counter()

print(counter())
print(counter())
print(counter())
print(counter())