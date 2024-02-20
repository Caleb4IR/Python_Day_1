# marks = [98, 75, 40, 80, 90, 45, 80, 60]

# # marks.pop()
# print(marks)
# print(type(marks))

# marks.pop(3)
# print(marks)

#marks[start:end]
#expected outcome - last threee to be removed

# end_index = len(marks) - 3
# print(end_index)
# print(marks[0:end_index]) # Does not mutate the original list
# print(marks)

# print(marks[0:-3])

# marks = [98, 75, 40, 80, 90, 45, 80, 60]
# # marks.remove(40) #mutation
# # print(marks)

# # eng = 88
# # marks.append(eng)
# # print(marks)

# sci = 85
# marks.insert(2, sci)
# print(marks)

# price_list1 = [1000,1500,400]
# price_list2 = [2000,500]
# print(price_list1 + price_list2) #No mutation

# print([5,6]*2) # [5,6,5,6]

#slice -> copy
#pop uses index, remove uses value

#copy
price_list = [1000,1500,400]
# price_list_copy = price_list
# print(price_list_copy)

# print(price_list_copy.append(600))
# print(price_list.append(700))

# print(price_list_copy, price_list)

price_list2 = price_list[:]
print(price_list)

print(id(price_list), id(price_list2))

subjects = ["eng", "maths", "science"]
print("".join(subjects))

#subjects.sort()
subjects.sort(reverse=True)
print(subjects)