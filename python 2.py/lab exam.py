# Repeated from question 5
def fibonacci_up_to(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=' ')
        a, b = b, a + b
    print()

# Test
limit = int(input("Enter limit for Fibonacci series: "))
fibonacci_up_to(limit)
