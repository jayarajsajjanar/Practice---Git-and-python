from gcd_lib import gcd_class

class fractions:
	def __init__(self,numerator,denominator):
		self.num=numerator
		self.den=denominator

	def display(self):
		print (self.num,"/",  self.den)

	def add_frac(self, sec_fraction):
		res_num = self.num*sec_fraction.den+self.den*sec_fraction.num
		res_den = self.den+sec_fraction.den
		gcd_object=gcd_class(res_num,res_den)
		gcd_object.gcd_self_disp()
		gcd_ret=gcd_object.gcd_func()
		print ("gcd_returned",gcd_ret)
		print (res_num/gcd_ret,"/",  res_den/gcd_ret)

#def gcd_func(numerator,denominator):


f1=fractions(1,2)
f2=fractions(1,2)

f1.display()
f2.display()

f1.add_frac(f2)