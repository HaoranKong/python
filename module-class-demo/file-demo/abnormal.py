from pathlib import Path


# print(" i will keep dividing the given two numbers.")
# print("Enter 'q' to quit.")

# while True:
#     try:
#         first_number=input("\nFirst number: ")
#         if first_number=='q':
#             break
#         second_number=input("Second number: ")
#         if second_number=='q':
#             break
#         answer=int(first_number)/int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)


path=Path('D:/python_STUDY/python/module-class-demo/file-demo/pi_digits.txt')
try:
    contents=path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    print(len(contents))
    print(len(contents.strip().split()))

    #在异常发生后，可以通过 pass
    # 关键字来表示什么都不做，这样既不会给出 traceback，也不会给出友好的错误提示：