def my_sum(m, n):
  if m == 0:
    return n
  if n == 0:
    return m  
  return (my_sum(m + 1, n - 1)) 
m = int(input())
n = int(input())
print(my_sum(m, n))
