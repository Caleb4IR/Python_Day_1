#One line functions
#They are anonymous - nameless function
#Implicitly return
#When you want to pass a function as an argument
#Best for 1 time use and for simple functions
# add = lambda a, b: a + b
# print(add(10, 20))

# #In Python a function is treated as a first class citizen(value)

# #1. Assign a function to a variable
# #2. Pass a function as argument
# #3. Return a function

# player_stats = [10, 30, 60]

# boosted_stats = map((lambda x: x * 2), player_stats)
# print(boosted_stats, list(boosted_stats))

# double_values = lambda x: x * 2
# boosted_stats = map(double_values, [10,30,60])

# def square(x):
#   return x * x

# super_boosted_stats = map(square, [10,30,60]) #normal function
# super_boosted_stats1 = map(lambda x: x * x, [10,30,60]) #When?
# print(list(super_boosted_stats))

# result1 = map(lambda x: x * 2, [(10,6),(30,8), (5,60)])
# print(list(result1))


# def fun(y):
#   x = 4 #1
# return x+y #3
# print(fun(5)) #2


# def say_hello():
#   return "Hello, "
# #"Greeting" becomes a higher order function for accepting a function as an argument
# #Thus map() is a higher order function
# def greeting(hello_message, name): #Accepting a function hello_message as argument hence
#   print(hello_message() + name)  #Use a function

# greeting(say_hello, "Caleb")

#Expected output [20,60,120]]
# def map_own(fn, arr):
#   result = []
#   for i in arr:
#     result.append(fn(i))
#   return result
# output = map_own(lambda x: x * 2, [10,30,60])

# print(output)

# #Or

# def map_own(fn, arr):
#   return [fn(i) for i in arr]

# output = map_own(lambda x: x * 2, [10,30,60])


# def sayHello1():
#   def msg():
#     return "Hello, 🎊"
#   return msg

# #Task 1
# msg_function = sayHello1()
# print(msg_function())

# #Task 2
# print(sayHello1()())

#Implicit return | factory function
#Functional programming

#What is currying and partials

mul = lambda x: lambda y: x * y #Everything after ":" is being returned
#pass 3 and 6
#Final output should be 18
result_function = mul(3)

# Call the returned lambda function with 6
final_output = result_function(6)

print("Final output:", final_output)

#Or

print(mul(3)(6))


result1 = map(lambda x: x * 2, [10,30,60])
result2 = filter(lambda x: x > 10, [10,50, 60, 100, 6, 8, 30])
print(list(result1))
print(list(result2))

#Pythonic way

#Sequence - Lisr
#1. len
#2. sum
#3. soted

print(sum([10,30,60]))
print(max([10,100,30,60]))
print(min([10,-1,30,60]))

print(all([True,False,True])) #and
print(any([True,False,True])) #or

print(all([10,0,30,-1]))

#Everything considered false
#1. 0
#2. []
#3. None
#4. {}
#5. " "
#6. set()
#7. ()
#8. False