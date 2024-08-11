# 1
# try:
#     a = int(input("Enter first number:"))
#     b = int(input("Enter second number:"))
#     c = a / b
#     if a == 0 or b == 0:
#         print("На ноль делить нельзя")
#     else:
#         print("Your answer is", c)    
# except ZeroDivisionError:
#     print("smth went wrong")        
# 2 
# try:
#     read_file = True
#     if read_file:
#         with open('pyt.txt', 'r') as read_op:
#               content = read_op.read(read_file)
#               print("your file is", content)
#     else:
#         print("file is empty")
# except FileNotFoundError:
#     print("file not found")
# 3
# try:
#     a = int(input("Enter int number:"))
#     b = a / 100
#     print("Your answer is", b)
# except ZeroDivisionError:
#     print("you entered schose 0")
# except ValueError:
#     print("you entered string ")
# 4 
# try:
#     read_file = "hello"
   
#     with open('pyt.txt', 'w') as read_op:
#               content = read_op.write(read_file)
#               print("your file is", content)

# except FileNotFoundError:
#     print("file not found")

# 5
# try:
#     a = input("Введите число: ")
#     b = int(a)
# except ValueError:
#     print("Это не целое число!")
# else:
#     print(f"Успешное преобразование! Вы ввели число {b}.")
# finally:
#     print("Программа завершена.")



    
   
     
              