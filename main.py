class Critten(object):
    """Моя зверушка"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    @property
    def mood(self):
        unhappines = self.hunger + self.boredom
        if unhappines < 5:
            m = "Отличное"
        elif unhappines <=10:
            m = "Хорошее"
        elif unhappines <= 15:
            m = "Нормальное"
        else:
            m = "Плохое"
        return m
    def talk(self):
        print("Меня зовут:", self.name, "\nУровень голода:", self.hunger, "\nНастроение:", self.boredom)
        self.__pass_time()
    def eat(self):
        food = int(input("Сколько еды вы хотите дать?"))
        if food == int():
            print("ВОзможно вы сделали что-то не так!")
            return self.eat()
        elif food == "":
            print("ВОзможно вы сделали что-то не так!")
            return self.food()
        print("Мррр, спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    def play(self):
        fun = int(input("Сколько часов вы хотите поигать?"))
        if fun == int():
            print("ВОзможно вы сделали что-то не так!")
            return self.fun()
        elif fun == " ":
            print("ВОзможно вы сделали что-то не так!")
            return self.fun()
        print("Уииии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
def main():
    crit_name = input("Назовите свою зверушку!: ")
    crit = Critten(crit_name)
    choice = None
    while choice != "0":
        print \
            ("""
            Моя зверушка

            0 - Выйти
            1 - Узнать самочувствие
            2 - Покормить
            3 - Поиграть
            """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()

        # feed your critter
        elif choice == "2":
            crit.eat()

        # play with your critter
        elif choice == "3":
            crit.play()

        # some unknown choice
        else:
            print("\nИзвините, но", choice, "нет в меню выбора")

main()
