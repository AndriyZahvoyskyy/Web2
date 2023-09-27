def create_queue():
    return[]
queue = create_queue()
lem_number = int(input("Введіть кількість чисел: "))

for index_number in range(lem_number):
    item = int (input("Введіть числa: "))
    queue.append(item)


num = int(input("Введіть кількість чисел для віднімання: "))
for index_item in range (num):
    item = queue.pop(0)

print("Ваші числа: ", queue)