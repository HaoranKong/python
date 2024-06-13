#字典
alien_0={'color':'green','points':5}
# print(alien_0['color'])
# print(alien_0['points'])



# del alien_0['points']
# print(alien_0)

# alien_0={}
# print(alien_0)
alien_0={'color':'green','speed':'slow'}
# print(alien_0['points'])
#KeyError: 'points'
#我们可以使用 get() 方法来避免错误的发生  d.get(key, [default])：根据键获取值

# print(alien_0.get('date'))

# favorite_languages={'jen':'python','sarah':'c','edward':'ruby','phil':'python'}
# for name,language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")
# for name in favorite_languages.keys():
#     print(name.title())
# for language in favorite_languages.values():
#     print(language.title())

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# alien_0={'color':'green','points':5}
# alien_1={'color':'yellow','points':10}
# alien_2={'color':'red','points':15}
# aliens=[alien_0,alien_1,alien_2]
# for alien in aliens:
#     print(alien)

pizza={'crust':'thick','toppings':['mushrooms','extra cheese']}
print(f"{pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    }
}
# for username,user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name=f"{user_info['first']} {user_info['last']}"
#     location=user_info['location']
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")

# name=input("What's your name? ")
# print(f"\nHello, {name}!")

# age=input("How old are you? ")
# # age=int(age)
# if age>=18:
#     print("\nYou are old enough to vote!")

# prompt="If you tell us who you are, we can personalize the messages you see."
# prompt+="\nEnter quit to end the program.\n"
# message=""
# while message!='quit':
#     message=input(prompt)
#     if message!='quit':
#         print("\n"+message)

current_number=0
while True:
    if current_number>5:
        break
    current_number+=1
    if current_number%2==0:
        continue 
    print(current_number)


# 可以尝试按 Ctrl+C 来结束程序的运行
# x=1
# while x<=5:
#     print(x)

unconfirmed_users=['alice','brian','candace']
confirmed_users=[]

while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses={1:2,3:4}
# while True:
#     name=input("\nWhat's your name? ")
#     response=input("\nWhat's your opinion? ")
#     responses[name]=response
#     if input("Have more?(yes/no)")=='no':
#         break
for name,response in responses.items():
    print(f"{name}'s opinpin is {response}")
