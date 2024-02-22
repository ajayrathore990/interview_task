import unittest

from agritech import SuperMarket

s= SuperMarket()


class CheckOutTest(unittest.TestCase):

	def setUp(self):
		self.supermarket= SuperMarket()

	def tearDown(self):
		pass

	def test_check_for_a(self):
		self.supermarket.item='A'
		assert self.supermarket.add_amount()==50

	def test_check_for_aa(self):
		self.supermarket.item='AA'
		assert self.supermarket.add_amount()==100

	def test_check_for_AAA(self):
		self.supermarket.item = 'AAA'
		assert self.supermarket.add_amount()==130

	def test_check_for_AAAB(self):
		self.supermarket.item='AAAB'
		assert self.supermarket.add_amount()==160

	def test_check_for_abcd(self):
		self.supermarket.item = 'ABCD'
		assert self.supermarket.add_amount()==115

	def test_check_for_aaaaaa(self):
		self.supermarket.item='AAAAAA'
		assert self.supermarket.add_amount()==260

	def test_check_for_aaabb(self):
		self.supermarket.item ='AAABB'
		assert self.supermarket.add_amount()==175

	def test_check_for_aaabbd(self):
		self.supermarket.item = 'AAABBD'
		assert self.supermarket.add_amount()==190

	def test_check_for_dababa(self):
		s=SuperMarket()
		self.supermarket.item= 'DABABA'
		assert self.supermarket.add_amount()==190


if __name__ == '__main__':
	unittest.main()