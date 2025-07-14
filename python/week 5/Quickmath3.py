

        # Define the Calculator class
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    def subtract(self, a, b):
        return a - b


my_calculator = Calculator()


sum_result = my_calculator.add(10, 5)
product_result = my_calculator.multiply(4, 6)
quotient_result = my_calculator.divide(20, 4)
difference_result = my_calculator.subtract(15, 7)


print("Addition:", sum_result)
print("Multiplication:", product_result)
print("Division:", quotient_result)
print("Subtraction:", difference_result)
