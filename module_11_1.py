# задание по теме "Обзор сторонних библиотек Python"
import requests
import numpy as np

# Создаем массив с помощью библиотеки numpy
array = np.array([6, 45, 3, 7, 56])

# Выполняем математические операции с массивом
# Возведение числа из массива в степень 2
squared_array = array ** 2

# Находим среднее арифметическое из всего массива
mean_value = np.mean(array)

# Вывод результатов

print("Дан массив:", array)
print("Возведение в степень 2:", squared_array)
print("Среднее арифметичекое всего массива:", mean_value)

# Используем библиотеку requests для запроса с сайта
response = requests.get('https://api.github.com')

# Проверяем правильность запроса
if response.status_code == 200:
    print("\nДанные с сайта github.com:")

    # Выводим HTTP-заголовки в ответе
    print(response.headers)

    # Получаем содержимое страницы
    print(response.content)

    # Выводим данные в формате JSON
    print(response.json())
else:
    print(f"Ошибка при запросе: {response.status_code}")
