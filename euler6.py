# Patrick Moore 2018-03-03
# Projec Euler Problem 6 (https://projecteuler.net/problem=6)

sumofsquares = 0                                 # variable to hold the value for the sum of the squares of the numbers
sum = 0                                          # variable to hold the value for the sum of the numbers 
squareofsum = 0                                  # variable to hold the value for the square of the sum of the numbers   
counter = 1                                      # this is the counter in the while loop
while counter != 101:                            # this will loop the numers 1 to 100 inclusive 
  sumofsquares,sum,squareofsum = sumofsquares + counter**2,sum + counter,sum**2 #increment all the values as per defined in the problem
  counter = counter + 1                          # increment the counter to move the problem on to the next term in the sequence 
print("The differnece between the sum of the squares and the square of the sums of the first 100 natural number is: ", str((squareofsum - sumofsquares)))
                                                 # line 11 prints the difference of the 2 final values 
                                                 # check does git work after mac os upgrade 