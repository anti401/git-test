# coding : utf-8

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_box1 = ["яблоко", "банан", "киви", "арбуз"]
fruits_box2 = ["персик", "банан", "ананас", "арбуз", "кокос"]

popular_fruits = [f for f in fruits_box1 if f in fruits_box2]
print('Популярные фрукты: ', popular_fruits)
