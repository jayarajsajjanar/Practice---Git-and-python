class fractions:
	def __init__(self,numerator,denominator):
		self.num=numerator
		self.den=denominator

	def display(self):
		print (self.num,"/",  self.den)

	def add_frac(self, sec_fraction):
		res_num = self.num*sec_fraction.den+self.den*sec_fraction.num
		res_den = self.den+sec_fraction.den
		print (res_num,"/",  res_den)

f1=fractions(1,2)
f2=fractions(1,2)

f1.display()
f2.display()

f1.add_frac(f2)