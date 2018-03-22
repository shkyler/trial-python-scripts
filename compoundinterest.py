def compoundinterest(principle,rate,term):
  while term != 0:
    principle = principle + (principle*rate)/100
    term = term - 1
  return(principle)

print(round(compoundinterest(1000,3,5),2))
print(round(compoundinterest(1000,7,10),2))