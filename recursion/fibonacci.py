# define the fibonacci() function below...
def fibonacci(n):
  if n == 0 or n == 1:
    return n
  return fibonacci(n-2) + fibonacci(n-1)



fibonacci(5)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"