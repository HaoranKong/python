# magicians=['alice','david','carolina']
# for magician in magicians:
#     print(magician.title()+', that was a great trick!')
#     print("I can't wait to see your next trick, "+magician.title()+".\n")
# print("Thank you, everyone. That was a great magic show!")

# 没有正确的缩进（缩进错误）
# 忘记缩进额外的代码行（逻辑错误）
# 循环后不必要的缩进（逻辑错误）
# 循环的末尾漏掉了冒号


# for value in range(1,5):
#     print(value)
#range([start,] end [,step])
# 代码只打印了数 1 ~ 4，
# 这是编程语言中常见的差一行为，输出在指定的第二个值处停止了。
# 要打印数 1 ～ 5，需要使用 range(1, 6)
# 第一个参数 start 是可选的：
# 例如 range(6) 将会打印数 0 ~ 5

# squares=[]
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)

# squares=[value**2 for value in range(1,11)]
# print(squares)

# digits=[1,2,3,4,5,6,7,8,9,0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# players=['charles','martina','michael','florence','eli']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])
# print(players[-3:])
# 切片（slice）：处理列表中部分元素的语法
# 我们可以通过在索引中添加冒号（:）来获取部分列表：

# players=['charles','martina','michael','florence','eli']
# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print (player.title())

# my_foods=['pizza','falafel','carrot cake']
# friend_foods=my_foods[:]
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)
# 切片操作总是返回列表的拷贝

# my_foods=['pizza','falafel','carrot cake']
# friend_foods=my_foods
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)


#元组 不可变的列表，使用圆括号而不是方括号来标识。
# dimensions=(200,50)
# print(dimensions[0])
# print(dimensions[1])
# dimensions[0]=250
# 试图修改元组的代码将导致错误

