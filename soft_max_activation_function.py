import math

# Euler's number
E = math.e

# Example list of outputs from the previous layer 
layer_outputs = [4.8, 1.21, 2.385]

# List to store the exponentiated values
exponentiated_values = []

# Calculate the exponentiated values (E^value) for each layer output
for output in layer_outputs:
    exponentiated_values.append(E**output)

# Calculating the sum of exponentiated values as our denominator 

#Our normalization function works like n1/Σn, n2/Σ, n3/Σn...

normalization_base = sum(exponentiated_values)

# List to store normalized values
normalized_values = []

# Normalize each exponentiated value by dividing by the sum
for exp_value in exponentiated_values:
    normalized_values.append(exp_value / normalization_base)

# Print the sum of the normalized values (should be close to 1.0)
print(sum(normalized_values))
