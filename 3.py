n = int(input("Введіть кількість елементів у списку:"))
my_list = []

for i in range(n):
    element = int(input("Введіть елемент: "))
    my_list.append(element)
new_list = []

for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(my_list)
print(new_list)
