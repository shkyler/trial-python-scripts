def newtonsroot(x):
  import random
  #r = random.randint(1,x)
  r = x/10
  iterations = 100
  while iterations != 0:
    r = r - (r**2 - x)/2*r
    iterations = iterations - 1
  return(r)

print(newtonsroot(100))
print(newtonsroot(144))