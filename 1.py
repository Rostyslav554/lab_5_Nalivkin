hat_list = [1, 2, 3, 4, 5]

hat_list[2] = int(input("Введіть  ціле число щоб замінити центральний номер у списку: "))

del hat_list[-1]

print("Довжина списку:", len(hat_list))

print("Оновлений список:", hat_list)
