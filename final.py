""" Structured English
This program opens the file Final.txt, which is a list of student grades on a final exam. 
It then creates a list, where each item of the list is a line of the file.
It displays the number of items in the list, which is the number of grades.
It then sums the grades in the list, and divides that by the number of grades to get an average.
It will display the average.
Then it will check each grade in the list and compare it to the average.
It will keep track of how many grades were above the average,
and display that number as a percentage of the number of grades.
"""

""" Pseudo-code
def main:
  file = Final.txt
  display(file)
  calculate_percent_above_avg(file)

def display(file):
  infile = open(file)
  listGrades = lines of file
  close file
  print(number of grades: )
  print(len(listGrades))
  avg = sum(listGrades) / len(listGrades)
  print(Average of grades: )
  print(avg)

def calculate_percent_above_avg(file):
  counter = 0
  for line in file
    if grade > avg
      counter +=1
  percentHigher = counter / len(listGrades)
  print(The percent of grades above average is: )
  print(percentHigher %)

main()
"""

def main():
  file = "Final.txt"
  calculate_percent_above_average(file)

def calculate_percent_above_average(file):
  infile = open(file, 'r')
  listGrades = [int(line.rstrip()) for line in infile]
  length = len(listGrades)
  sum1 = sum(listGrades)
  avg = sum1 / length
  print("Number of grades:", length)
  print("Average grade:", avg)
  counter = 0
  for item in listGrades:
    if item > avg:
      counter += 1
  percentHigher = counter / length
  print("Percent of grades above average:", end= " ")
  print("{0:.2%}".format(percentHigher))

main()

