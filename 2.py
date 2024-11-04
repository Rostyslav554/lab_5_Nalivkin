n = int(input("Введіть кількість елементів у списку:"))
my_list = []

for i in range(n):
    element = int(input("Введіть елемент: "))
    my_list.append(element)

for i in range(len(my_list) - 1):
    swapped = False
    for j in range(len(my_list) - 1 - i):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            swapped = True
    if not swapped:
        break

print(my_list)