numbers = [8,10,6,2,4]
n = len(numbers)
count = 0
for i in range(len(numbers)-1):
    for j in range(len(numbers)- 1):
        count += 1
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)
print(count)

# numbers = [1,2,3,4,5] #[8,10,6,2,4]
# n = len(numbers)
# count = 0
# while swapped:
#     swapped = False
#     for i in range(len(numbers)-1):
#         for j in range(len(numbers)- 1):
#             count += 1
#             if numbers[j] > numbers[j + 1]:
#                 swapped = True
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print(numbers)
# print(count)

#   sort
# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)

my_list = [10,8,6,4,2]
new_list = my_list[-1:1]
print(new_list)

del my_list[:]
print(my_list)

