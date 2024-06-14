# 类的学习
class Dog:
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age,color):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

# my_dog=Dog('willie',6,'black')
# your_dog=Dog('lucy',3,'white')  
# my_dog.sit()

# print(f"My dog's name is {my_dog.name.title()}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()

# print(f"\nYour dog's name is {your_dog.name.title()}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()

class Car:
    """模拟汽车"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def _init_(self,make,model):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.odometer_reading=0
    def get_description_name(self):
        """返回整洁的描述信息"""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """将里程表读数设置为指定的值"""
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading+=miles
# my_new_car=Car('audi','a4',2019)   
# my_new_car.update_odometer(23_500)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()
# print(my_new_car.get_description_name())
# my_new_car.read_odometer()

# my_new_car.odometer_reading=2
# my_new_car.read_odometer()

# my_new_car.update_odometer(22)
# my_new_car.read_odometer()


class ElctricCar(Car):
    """电动车的独特之处"""
    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        self.battery_size=75
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def fill_gas_tank(self):
        """电动车没有油箱"""
        print("This car doesn't need a gas tank!")
    def get_description_name(self):
        """返回整洁的描述信息"""
        long_name=f"{self.year} {self.make} {self.model}{self.battery_size}"
        return long_name.title()

# my_tesla=ElctricCar('tesla','model s',2019)
# print(my_tesla.get_description_name())
# my_tesla.describe_battery()
# print(my_tesla.get_description_name())

class batt