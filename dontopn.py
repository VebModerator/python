"""
ООП - объектно ориентированное программирование
класс - общее описание предметной области на языке прогаммирования
объект - экземпляр (конкретный представитель класса)
метод - функция, свзяанная с объектом класса (классом)
атрибут - хар-ка (с-во) объекта или класса
конструктор - метод, который управляет созданием объекта

инкапсуляция - механизм, позволяющий скрывать внутренние детаци реализации объекта
и предоставлять доступ к ним только через определенные методы, чтобы защитить
данные и контролировать доступ к ним
"""

class Car:
    _COLORS = ("red","green","blue")
    def __init__(self, brand, model, year, power, currence="RUB"):
        self.brand = brand
        self.model = model
        self.year = year
        self.power = power
        self.country = "Armenia"
        self.currence = currence
        self.is_power = False

        #законченный атрибут
        self._color = ""
        self.__speed = ""

    #метод объекта
    def go(self):
        if self.is_power:
            print(f"{self.brand} {self.model} TO GO!")
        else:
            print("Car must be POWER ON")

    def stop(self):
        if self.is_power:
            print(f"{self.brand} {self.model} STOP")
        else:
            print("Car must be POWER OFF")

    def turn(self, direction):
        if self.is_power:
            print(f"{self.brand} {self.model} TURN! {direction}")
        else:
            print("Car must be POWER ON")

    def power_on(self):
        if self.is_power:
            print("Car already is POWER ON!")
        else:
            print(f"{self.brand} {self.model} POWER ON!")
            self.is_power = True


    def power_on(self, new_color):
        if self.is_power:
            print("Car already is POWER OFF!")
        else:
            print(f"{self.brand} {self.model} POWER OFF!")
            self.is_power = False


#Дочерний класс грузовых машин
class Truck(Car):
    #указывание характеристики родительского класса и новые характеристики дочернего
    def __init__(self, brand, model, year, power, capcity, currence="RUB"):
        #Вызываем конструктор родительского класса с его параметрами серез функцию super
        super().__init__( brand, model, year, power, capcity, currence="RUB")
        self.capcity = capcity
        self.axles = axles

    def tilt_trailer(self):
        print(f"{self.brand} {self.model} title trailer")

    def poerw_off(self):
        super()._power_off()
        print("The method of truck class")

car_audi = Car(brand="Audi", model = "A6", year = "2022", power = "249")
car_bmw = Car(brand="BMW", model = "X6", year = "2022", power = "249")

truck = Truck(brand="Volvo", model="xaxaxa", year="2019", capcity="4000", axles="6", power="700")
truck.power_on()
truck.tilt_trailer()
truck.power_off()







car_audi.power_off()
car_audi.go()
car_audi.turn(direction="left")

car_audi.power_on()
car_audi.power_on()
car_audi.go()
car_audi.turn(direction="left")
car_audi.power.off()

car_audi._color(new_color="green")
car_audi._display_color()

print(dir (car_audi))
print(car_audi_Car_speed)

print(id(a))