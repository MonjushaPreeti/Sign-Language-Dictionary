import unittest
import dictionary
import os
class TestSearch(unittest.TestCase):

	"""
	  This is a  class whose instances are single test cases.It has a by default method run tests
      By default, the test code itself should be placed in a method named 'runTest'.
	"""

	def test_Input(self):
		"""
		This function is going to match the text input (be careful) with the image (be careful.image)
		and after running test case has it passed or failed , will show it.
		:param: self . This is going to create a instance of it's own and run the test case.
		:return:OK(passed) or FAILED .
        This is also going to show how many tests it ran
		"""
		s = 'https://i.ibb.co/D9TXbyH/a.jpg'
		actualOutput=dictionary.search("a")


		self.assertEqual(actualOutput,s)



if __name__ == '__main__':
	unittest.main()