def squares_of_first_n_natural_numbers(n):
  """Calculates and prints the squares of the first n natural numbers."""

  if n < 1:
    print("Please enter a positive integer.")
  else:
    print("The squares of the first", n, "natural numbers are:")
    for i in range(1, n + 1):
      square = i * i
      print(square)

n = int(input("Enter a positive integer: "))
squares_of_first_n_natural_numbers(n)