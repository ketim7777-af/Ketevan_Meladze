
def even_numbers():
    num = 0

    while True:
        yield num
        num += 2
      
numbers = even_numbers()

count = 0
for num in numbers:
    print(num)
    count += 1
    if count == 10:
        break


