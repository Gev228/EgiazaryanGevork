number = int(input())
m=number
p=0
i=0
while m>0:
  i=m % 10
  p=p*10+i
  m=m // 10
if number==p:
  print("это палиндром")
else:
  print("не полиндром")
