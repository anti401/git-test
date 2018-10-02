# coding : utf-8

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.

N = int(input('Введите номер комнаты - '))

# s - номер блока (1х1, 2х2, 3х3 и т.д.), из которых состоит башня
# n - наибольший номер комнаты в блоке (сквозной), f - верхний этаж блока
n = 0
f = 0
s = 0
while n < N:
	s += 1
	f += s
	n += s**2

floor = f - (n - N) // s
print('Этаж: ', floor)
num_on_floor = s - (n - N) % s
print('Номер на этаже: ', num_on_floor)
