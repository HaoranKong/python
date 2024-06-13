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
