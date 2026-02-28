# SIMPLE Calculator project
# Define arithmetic functions
def add(a, b):
  result = a + b
  return result

def subtract(a, b):
  result = a - b
  return result

def multiply(a, b):
  result = a * b
  return result

def divide(a, b):
  result = a / b
  return result

def exp(a, b):
  result = a ** b
  return result

# Test calling each function with really basic input
print(add(4, 2))
print(subtract(4, 2))
print(multiply(4, 2))
print(divide(4, 2))
print(exp(4, 2))
