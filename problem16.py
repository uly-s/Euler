from math import factorial

# Calculate central binomial coefficients for n from 1 to 10
central_binomial_coefficients = [factorial(2*n) // (factorial(n) ** 2) for n in range(1, 21)]

# Create a list of (n, coefficient) pairs for easy reading
n_coefficient_pairs = list(enumerate(central_binomial_coefficients, start=1))

print(n_coefficient_pairs)