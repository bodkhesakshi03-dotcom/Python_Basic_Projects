square = lambda x: x**2

try:
    numbers = list(range(1, 21))
    squares = [square(n) for n in numbers]
    even_squares = [sq for sq in squares if sq % 2 == 0]
    
    print("Squares:", squares)
    print("Even Squares:", even_squares)
except Exception as e:
    print("Error:", e)
