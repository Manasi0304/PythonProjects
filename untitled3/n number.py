
n = int(input("Enter how many numbers you want to sort: "))
if n < 2:
    print("Please enter at least 2 numbers.")
numbers = []
for i in range(n):
    while True:
        try:
            num = int(input(f"Enter number {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            swapped = True
    if not swapped:
        break
print("Numbers in ascending order:", *numbers)

