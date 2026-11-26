# def add_numbers(x, y):
#     return x + y
# x = input("Enter a value x: ")
# y = input("Enter a value y: ")
# reult = add_numbers(int(x), int(y))
# print(f"The sum of {x} and {y} is: {reult}")

# tempareature = int(input("Enter a temperature: "))
# if tempareature > 30:
#     print("It's a hot day")     
# elif tempareature > 20:
#     print("It's a nice day")
# else:
#     print("It's a cold day")
# print("weather report ended")

weight = int(input("Enter your weight: "))
message = "You are overweight" if weight > 80 else "You are Good" if weight < 80 and weight > 70 else "You are Underweight"
print(message)