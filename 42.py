import pandas as pd

# загружаем данные из файла
data = pd.read_csv('https://raw.githubusercontent.com/dkon0v/Lesson9GB/main/california_housing_train.csv')

# получаем минимальное значение population
min_pop = data['population'].min()

# получаем максимальное значение households в зоне минимального значения population
max_households = data.loc[data['population'] == min_pop]['households'].max()

# выводим результат
print(f"Максимальное значение households в зоне минимального значения population ({min_pop}): {max_households}")
