
import random #Подгружаем библиотеку случайных вычислений

game = ["камень", "ножницы", "бумага"]#Сюда можно добавлять новые элементы игры

Ruslan = input('Введите значение для Руслана: ')
Timur = game[random.randint(0, len(game)-1)]#За Тимура будет отдуваться ЭВМ
if Timur == "камень" and Ruslan == "ножницы":
    print('Победа Тимура')
elif Timur == "бумага" and Ruslan == "камень":
    print('Победа Тимура')
elif Timur == "ножницы" and Ruslan == "бумага":
    print('Победа Тимура')
elif Timur == Ruslan:
    print('Ничья')
else:
    print('Победа Руслана')