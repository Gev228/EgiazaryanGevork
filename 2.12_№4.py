def my_power(a,n): 
  if a == 0: 
    return(a) 
  if n == 0: 
    return 1 
  else: 
    return a*my_power(a,n-1) 
a=int(input()) 
n=int(input()) 
print(my_power(a,n)) 
