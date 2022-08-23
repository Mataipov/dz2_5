import random
from decouple import config

MY_MONEY = config("MY_MONEY", cast=int)
mas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

def res():
    global MY_MONEY
    stav = int(input("Введите ставку: "))
    slot = input("Введите слот: ")
    if random.choice(mas) == slot:
        print("вы выйгралии")
        MY_MONEY += stav*2
    else:
        print("Вы проиграли")

        MY_MONEY -= stav

def start_game():
    res()
    while True:
        again = input("Сыграем еще? (да/нет): ")
        if again == "да":
            res()

        else:
            print(MY_MONEY)
            break