# even / odd num check

# Loop game
while True:
    # Enter a number here
num = int(input("Enter a number: "))

# Modulo operator to check whether num is even or odd
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")
