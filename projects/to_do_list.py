todo_list = []

while True:
    task = input("Add a task (or type 'quit'): ")
    if task.lower() == 'quit':
        break
    todo_list.append(task)

print("Your Tasks:")
for idx, t in enumerate(todo_list, 1):
    print(f"{idx}. {t}")
