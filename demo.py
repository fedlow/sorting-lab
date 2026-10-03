from sorts import bubble_sort, selection_sort, insertion_sort

data = [5, 2, 9, 1, 5, 6, 0, -3, 8, 4]

print("Исходный:      ", data)
print("Пузырьком:     ", bubble_sort(data))
print("Выбором:       ", selection_sort(data))
print("Вставками:     ", insertion_sort(data))