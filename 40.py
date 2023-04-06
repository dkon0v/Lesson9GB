#Работать с файлом california_housing_train.csv, который находится в папке sample_data. 
#Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

import pandas as pd

# Чтение данных из csv-файла

df = pd.read_csv('https://github.com/dkon0v/Lesson9GB/blob/main/california_housing_train.csv')

## Выбор только тех строк, где количество людей от 0 до 500

df = df[df['population'] <= 500]

# Вычисление средней стоимости дома

mean_house_value = df['median_house_value'].mean()

print(f" Средняя стоимость дома, где количество людей от 0 до 500: ${mean_house_value:,.2f}")
