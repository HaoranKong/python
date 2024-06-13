# def greet_user():
#     name="konghaoran"
#     """显示简单的问候语"""
#     print(f"Hello! {name.upper()}!")
# greet_user()

# def describe_pet(animal_type,pet_name):
#     """显示宠物的信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('hamster','harry')

# describe_pet(pet_name='harry',animal_type='dog')

# def describe_pet(pet_name,animal_type='dog'):
#     """显示宠物的信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(pet_name='harry')

#关键词实参必须放在位置实参后面

# def get_formatted_name(first_name,last_name,middle_name=''):
#     """返回整洁的姓名"""
#     if middle_name:
#         full_name=f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name=f"{first_name} {last_name}"
#     return full_name.title()
# musician=get_formatted_name('jimi','hendrix')
# print("\n"+musician)

# def get_formatted_name(first_name,last_name,middle_name=''):
#     """返回整洁的姓名"""
#     if middle_name:
#         full_name=f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name=f"{first_name} {last_name}"
#     return full_name.title()
# musician=get_formatted_name('jimi','hendrix','lee')
# print("\n"+musician)
# musician=get_formatted_name('jimi','hendrix')
# print("\n"+musician)

# def build_person(first_name,last_name,age=''):
#     """返回一个字典，其中包含一个人的信息"""
#     person={'first':first_name,'last':last_name}
#     if age:
#         person['age']=age
#     return person
# musician=build_person('jimi','hendrix',age=27)
# print(musician)
# musician=build_person('jimi','hendrix')

# def get_formatted_name(first_name,last_name):
#     """返回整洁的姓名"""
#     full_name=f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name=input("First name: ")
#     if f_name=='q':
#         break   
#     l_name=input("Last name: ")
#     if l_name=='q':
#         break
#     formatted_name=get_formatted_name(f_name,l_name)
#     print(f"\nHello, {formatted_name}!")


# def greet_users(names):
#     """向列表中的每位用户都发出简单的问候"""
#     for name in names:
#         msg=f"Hello, {name.title()}!"
#         print(msg)

# usernames=['hannah','ty','margot']
# greet_users(usernames)

# def verify_users(unconfirmed_users,confirmed_users):
#     """验证用户直到没有未验证用户为止，将每个经过验证的用户都移到已验证用户列表中"""
#     while unconfirmed_users:
#         current_user=unconfirmed_users.pop()
#         print(f"Verifying user: {current_user.title()}")
#         confirmed_users.append(current_user.title())
# def show_confirmed_users(confirmed_users):
#     """显示所有已验证用户"""
#     print("\nThe following users have been confirmed:")
#     for confirmed_user in confirmed_users:
#         print(confirmed_user)

# unconfirmed_users=['alice','brian','candace']
# confirmed_users=[]
# verify_users(unconfirmed_users[:],confirmed_users)
# show_confirmed_users(confirmed_users)
# print(unconfirmed_users)

# def make_pizza(*toppings):
#     """打印顾客点的所有配料"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')

# def make_pizza(size,*toppings):
#     """概述要制作的披萨"""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza(16,'pepperoni')
# make_pizza(12,'mushrooms','green peppers','extra cheese')

def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)
