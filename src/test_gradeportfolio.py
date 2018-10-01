# test_gradeportfolio
import unittest

from gradeportfolio import GradePortfolio

class TestGradePortfolioMethods(unittest.TestCase):

	def test_init(self):
		test = GradePortfolio('../data/grade-data.json')

	def test_AverageGrade(self):
		test = GradePortfolio('../data/grade-data.json')
		self.assertEqual(test.AverageGrade(), 'B')

	def test_AverageGradeDifference(self):
		test = GradePortfolio('../data/grade-data.json')
		self.assertEqual(test.AverageGradeDifference(), 5.842696629213483)

	def test_FemaleCount(self):
		test = GradePortfolio('../data/grade-data.json')
		self.assertEqual(test.FemaleCount(), 17)

	def test_MaleCount(self):
		test = GradePortfolio('../data/grade-data.json')
		self.assertEqual(test.MaleCount(), 72)			