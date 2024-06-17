from random import choice
from car import ElctricCar as EC,Car as C
my_new_car=C('audi','a4',2019)
print(my_new_car.get_description_name())

my_tesla=EC('tesla','model s',2019)
print(my_tesla.get_description_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

players=['charles','martina','michael','florence','eli']
my_dict = {'player1': players[0], 'player2': players[1], 'player3': players[2]}
my_dict['player4'] = players[3]
print(my_dict)
print(players[0:3])
print(choice(my_dict))