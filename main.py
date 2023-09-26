
input_data = input("Введите данные для диаграммы, разделенные пробелом: ").split()


max_value = max(map(int, input_data))

# Создаем диаграмму в консоли с использованием символов '*' и границ
for row in range(max_value, 0, -1):
    row_data = ['*' if int(value) >= row else ' ' for value in input_data]
    print(" ".join(row_data))

# Выводим подписи оси X
x_labels = " ".join(str(i + 1) for i in range(len(input_data)))
print(x_labels)
