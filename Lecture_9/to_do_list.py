
def add_task(task_name, task_list=[]):
    task_list.append(task_name)
      
    print(task_list)
      
add_task("Meeeting with boss")
add_task("Meeeting with Mari")
add_task("Go home")       

# ცარიელი სია მხოლოდ ერთხელ იქმნება ფუნქციაში.
# ფუნქციის ყოველი გამოძახებისას იგივე სია გამოიყენება,
# ამიტომ ახალი დავალებები წინა დავალებებს ემატება.

# Task B

def add_task(task_name, task_list=None):
    if task_list is None:
        task_list = []

    task_list.append(task_name)

    print(task_list)

add_task("Meeting with boss")
add_task("Meeting with Mari")
add_task("Go home")


# ფუნქციის ყოველი გამოძახებისას ახალი ცარიელი სია იქმნება.
# ამიტომ თითოეულ სიაში წინა დავალებები არ ინახება,
# მხოლოდ მიმდინარე დავალება ემატება.

    
