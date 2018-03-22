# Patrick Moore 2018-02-27
# Iris Data Set - (http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)
# Reference for the problem - (https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) fromt the Python Tutorial
# This is not a problem from the problem sets - this was me trying to get the average of a column from the iris data file
with open("data/iris.csv", "r") as myfile:                         
  sums = 0
  mean = 0 
  counter = 0
  for line in myfile:
    rows = line.split(',')[0:5] 
    sums = sums + float(rows[0]) 
    counter = counter + 1
  mean = sums/counter
  print("The average sepal lenght is: " + str(round(mean,2)) + " cms")

