'''''
import random
x = random.randint(1, 40)
y = random.randint(1, 40)
z = x + y
ans = input(f"what is the sum of {x} and {y}?")

while int(ans) != int(z):
    ans = input(f"Try again! What is the sum of {x} and {y}?")
print("Correct")
'''''
import random
def calculate_sum(x, y):
    return x + y
def calculate_diff(x, y):
    return x - y
def calculate_prod(x, y):
    return x * y
def calculate_qnt(x, y):
    return x / y
x = random.randint(1, 10) 
y = random.randint(1, 10) 
prompt = input("choose the type of questiom: ")
if str(prompt) == "sum":
    ans = input(f"What is the sum of {x} and {y}? ")
    while int(ans) != calculate_sum(x, y):
      ans = input(f"Try again! What is the sum of {x} and {y}?")
    print("Correct!")
elif str(prompt) == "diff":
    ans = input(f"What is the difference of {x} and {y}?")
    while int(ans) != calculate_diff(x, y):
        ans = input(f"try again! What is the difference of {x} and {y}?")
    print("Correct!")
elif str(prompt) == "prod":
    ans = input(f"What is the product of {x} and {y}?")
    while int(ans) != calculate_prod(x, y):
        ans = input(f"try again! What is the product of {x} and {y}?")
    print("Correct!")
elif str(prompt) == "qnt":
    ans = input(f"What is the quotient of {x} and {y}?")
    while float(ans) != calculate_qnt(x, y):
        ans = input(f"try again! What is the quotient of {x} and {y}?")
    print("Correct!")

