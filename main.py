prices = [100, 250, 450, 1200, 850]
discounted = list(map(lambda x: round(x * 0.85, 2), prices))
print(discounted)  # [85.0, 212.5, 382.5, 1020.0, 722.5]

celsius = [0, 20, 37, 100, -5]
fahrenheit = list(map(lambda c: round(c * 9/5 + 32, 1), celsius))
print(fahrenheit)  # [32.0, 68.0, 98.6, 212.0, 23.0]
