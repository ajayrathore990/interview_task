values  = {"A":50,"B":30,"C":20,"D":15}


class SuperMarket:
	def __init__(self):
		self.item=''
		self.discount=0

	def a_discount(self):
		base_discount=1
		base_discount_a=0
		base_discount_b=0

		#import pdb;pdb.set_trace()
		new_string = self.item

		''' check for discount  for A string condition'''
		if "A" in self.item:
			discount_a, a_string = divmod(self.item.count('A'),3)
			if discount_a>=1 :
				base_discount_a= discount_a*130
				new_string = self.item.replace('A','')

				if a_string >0:
					new_string = new_string + a_string*'A'

		''' check for discount for B string condition'''

		if "B" in self.item:
			discount_b, b_string = divmod(self.item.count('B'),2)

			if discount_b>=1 :
				base_discount_b = discount_b*45
				new_string = new_string.replace('B','')
				if b_string >0:
					new_string = new_string + a_string*'B'

		base_discount =base_discount_a + base_discount_b


		return base_discount, new_string

	def add_amount(self):
		''' check for empty string string condition'''
		if self.a_discount()[1] =='':
			return abs(self.a_discount()[0])

		for item in self.a_discount()[1]:
			if item in values.keys():
				self.discount =	self.discount + values[str(item)]
				re= self.discount+self.a_discount()[0]
		return abs(re)
