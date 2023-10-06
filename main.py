import matplotlib.pyplot as plt
data = []
num_values = int(input("Введіть кількість значень: "))
for i in range(num_values):
    value = float(input(f"Введіть значення {i + 1}: "))
    data.append(value)
plt.bar(range(len(data)), data)
plt.xlabel('Категорії')
plt.ylabel('Значення')
plt.title('Стовпчаста діаграма')
plt.show()
