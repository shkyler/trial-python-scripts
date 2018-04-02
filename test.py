def sum(x,type):                                      # sum(x) is a function that takes an argument of 'x' and then returns the sum of the values in column 'x'
  with open("data/iris.csv", "r") as myfile:     # this statement opens the iris data set as an object called myfile                  
    sums = 0                                     # this initialises a variable that will used to store the values of the sum
    for line in myfile:                          # this loop run through the rows of the file one at a time
      rows = line.split(',')[0:5]
      if type == 'all':
        sums = sums + float(rows[x])
      else:
        if type in rows[4]:                # rows is a new string that temporarily stores the data values from each line split into seperate entries per column of the data set
          sums = sums + float(rows[x])               # on each pass through the loop sums is incremented with the float value of the line for the column specified by 'x'
    return sums                                  # the final value of the sum is returned with the summation of all values in the specified column

def count(x,type):
  with open("data/iris.csv", "r") as myfile:     # this statement opens the iris data set as an object called myfile                  
    counter = 0                                     # this initialises a variable that will used to store the values of the sum
    for line in myfile:  
      rows = line.split(',')[0:5]
      if type == 'all':
        counter = counter + 1
      else:
        if type in rows[4]:
          counter = counter + 1  
    return counter

def mean(x,type):
  avg = sum(x,type)/count(x,type)
  return avg

#print(round(sum(0,'setosa'),2))
#print(round(sum(0,'versicolor'),2))
#print(round(sum(0,'virginica'),2))
#print(round(sum(0,'all'),2))

#print(count(0,'all'))
#print(count(0,'setosa'))
#print(count(0,'versicolor'))
#print(count(0,'virginica'))

#print(round(mean(0,'setosa'),2))
#print(round(mean(0,'versicolor'),2))
#print(round(mean(0,'virginica'),2))
#print(round(mean(0,'all'),2))

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16])
plt.ylabel('some numbers')
plt.show()
