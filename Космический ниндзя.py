import random
import datetime
import time


class Alien:
    alien = {"Зорк'хала" : (100, 50),
             "Треблус" : (100, 50),
             "Ксар'иан" : (100, 50),
             "Пак'такен" : (100, 50),
             "Глир'зон" : (100, 50)
             }
    def __init__(self):
        self.name = random.choice(tuple(self.alien.keys()))
        self.hp, self.dmg = self.alien[self.name]

    def attack(self):
        slova = ("Абра-кадабра","Сникерс","Арбуз","Паровоз","Экскаватор")
        random_slova = random.choice(slova)
        return random_slova

def time1():
    time = datetime.datetime.now().timestamp()
    return time

score = 0
print("Привет, игра началась!")

while True:
    victim = Alien()
    print(f"Вы встретили пришельца {victim.name}, его здоровье {victim.hp} а урон {victim.dmg}")
    action = victim.attack()
    print(f"Пришелец наносит атаку: {action}")
    t1 = time1()
    slovo = input("")
    t2 = time1()
    if slovo.lower() != action.lower():
        print("Вы ввели слово неправильно")
        break
    if t2 - t1 >= 10:
        print("Вы не успели отбить атаку, и проиграли!")
        break
    else:
        score += 1
        print(f"Вы успешно отбились '{victim.name}' перед тем, как пришелец атаковал!")
        print(f"Ваш текущий счет: {score} очков")
        time.sleep(2)

print(f"Игра окончена! Ваш итоговый счет: {score} очков.")


