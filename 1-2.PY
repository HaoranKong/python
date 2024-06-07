"""
This script contains various examples of Python code.

The code demonstrates the following concepts:
- Printing messages
- Manipulating strings
- Using escape characters
- Stripping whitespace from strings
- Defining and using functions
- Working with numbers and arithmetic operations

"""

# print("Hello, World!")

# name='ada lovelace '
# print(name.title())
# print(name.upper())
# print(name.lower())

# first_name='ada'
# last_name='lovelace'
# full_name=f"{first_name}   {last_name}"
# print(full_name)

# message=f"Hello, {full_name.title()}!"
# print(message)

# print("python rust")
# print("python\nrust")   #\n is the abbreviation for newline character
# print("\tpython\n\trust")   #\t is the abbreviation for tab character

# 'iTruing'.lstrip()   #remove the whitespace from the left side
# 'iTruing'.rstrip()   #remove the whitespace from the right side
# 'iTruing'.strip()   #remove the whitespace from both sides

# url="https://www.baidu.com"
# def strip_url_prefix(url):
#     url=url.strip('https://')
#     return url

# # url = strip_url_prefix(url)
# print(url)

# message="One of Python's strengths is its diverse community."
# print(message)

# print('hello'+"""\nehllp""")
# print("hello"*2)

# print (3/2)
# print (3//2)

# print(1000000)
# print(1_000_000)
# print(1000000.5)
# print(1_000_000.5)

# # Add an integer and a float
# print(2.5 + 2)   # The result is 4.5

# print(3/3)  # The result is 1.0 float
# # Perform integer division
# print(3//3)  
# print(2.5//2)  #返回商的整数部分 向下取整
# print(1.5**2)  #返回x的y次幂
# print(1.5%2)  #返回x除以y的余数
# print(True)
# print(False)
# print(True and False)
# print(True or False)


# print(3/0)  # ZeroDivisionError: division by zero

# print(3/0.0)  # The result is inf

# print(0.0/0.0)  # The result is nan

x,y,z=0,0,0
print(x==0 and y==0 and z==0)
print(x,y,z)

MAX_CONNECTIONS=5000
print(MAX_CONNECTIONS)

