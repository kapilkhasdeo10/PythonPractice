# # question 1
# largest_number = -99999999

# number = int(input("Enter a number or type -1 to stop: "))

# while number != -1:
#     if number > largest_number:
#         largest_number = number
#     number =int(input("Enter a number or type -1 to stop: "))
    
#     print("The largest number is:", largest_number)
    
# question 2
a = int (input("enter a number"))
count = 1
even = 0
odd = 0
while count <= a:
    if count %2 == 0:
        even += 1
    else: odd += 1
    count += 1
print("Even: ",even)
print("odd: ",odd)
