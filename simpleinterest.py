def simpleinterest(principle, rate, term):
  principle = principle + (principle * rate * term)/100
  return principle

print(round(simpleinterest(1000,3,5),2))
print(round(simpleinterest(1000,7,10),2))