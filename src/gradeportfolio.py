# Gallegos Isaac Homework 3
# September 26th, 2018
# Gavin and Greg helped me with properly using dictionaries

import os
import json

class GradePortfolio:

	''' The constructor initializes the data and provides a reference dictionary to aid in quantifying the letter grades of the dataset '''
	def __init__(self, FileLocation = '../data/grade-data.json'):
		self.data = []
		with open(FileLocation) as f:
		    self.data = json.loads(f.read())
		self.grades = {'A':90, 'B':80, 'C':70, 'D':60, 'F':50}

	''' Calculates average grade from every students final grade. Achieves this by looping through every student and using the grade dictionary to quantify their letter grade to an integer.'''
	def AverageGrade(self):
		count = 0
		for i in self.data:
			count = count + self.grades[i[3]]
		average = int(count/len(self.data))
		for i in self.grades:
			if average == self.grades[i]:
				return i

	''' Calculates average difference in grades between midterm and final for each student. The result gives a floating point difference that equates to a little more than half a letter grade '''
	def AverageGradeDifference(self):
		differences = []
		for i in self.data:
			x = self.grades[i[2]]
			y = self.grades[i[3]]
			z = abs(y-x)
			differences.append(z)
		count = 0
		for i in differences:
			count = count + i
		average = count/len(differences)
		return average

	''' Calculates the number of female students in the dataset '''
	def FemaleCount(self):
		count = 0
		for i in self.data:
			if i[1] == 'F':
				count = count + 1
		return count

	''' Calculates the number of male students in the dataset '''
	def MaleCount(self):
		count = 0
		for i in self.data:
			if i[1] == 'M':
				count = count + 1
		return count

if __name__ == '__main__':

	''' Here I call all the functions '''
	value = GradePortfolio()
	print ()
	print ('Average Grade:', value.AverageGrade())
	print ('Average Change in Grade:', value.AverageGradeDifference(), 'or about half a letter grade')
	print ('Number of Females:', value.FemaleCount())
	print ('Number of Males:', value.MaleCount())