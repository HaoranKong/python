#判断
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
car = 'audi'
print(car=='Audi')
print(car.title()=='Audi')


age=17
if age>=18:
    print("You are old enough to vote!")
elif age<18:
    print("Sorry, you are too young to vote.")
else:
    print("You are old enough to vote!")

#也可以将列表名作为条件表达式，只有非空才为true
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#使用多个列表
available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
