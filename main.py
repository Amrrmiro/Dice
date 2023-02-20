import random

start_num = int(input("Enter the starting number: "))
end_num = int(input("Enter the ending number: "))

if end_num < start_num:
    print("Error: The ending number must be greater than the starting number.")
else:
    random_number = random.randint(start_num, end_num)
    print(f"The random number is: {random_number}")