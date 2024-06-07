# bikes=['trek','redline','giant']
# print(bikes)
# print(bikes[0])
# print(bikes[2],bikes[-1])

# bicyckes=['trek','cannondale','redline','specialized']
# message=f"My first bicycle was a +{bicyckes[0].title()}+"

# bicyckes[0]='1'
# print(bicyckes)

# bicyckes.append('2')
# print(bicyckes)

# bikes=[]
# bikes.append('trek')
# bikes.insert(1,'redline')
# print(bikes)

# bikes=['trek','redline','giant']
# del bikes[0]
# print(bikes)

# bikes=['trek','redline','giant']
# poped_bike=bikes.pop(0)
# print(bikes.pop())
# print(bikes)
# print(poped_bike)


motorcycles=['honda','yamaha','suzuki']
too_expensive='suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

nums=[9,6,3,7,2,1,8,5,4]
# print(sorted(nums))
# print(nums)

# nums.sort()
# print(nums)

# nums.sort(reverse=True)
# print(nums)

nums.reverse()
print(nums)

print(len(nums))