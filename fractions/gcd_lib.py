class gcd_class:
	"""docstring for  """
	def __init__(self, numerator, denominator):
		#super( , self).__init__()
		self.num = numerator
		self.den = denominator

	def gcd_self_disp(self):
		print (self.num,self.den)

	def  gcd_func(self):
		#return self.num
		#return self.den
		for i in range(1,self.num+1):
			if self.num%i == 0:
				maxdiv_num = i

		for i in range(1,self.den+1):
			if self.den%i == 0:
				maxdiv_den = i
		
		if maxdiv_den > maxdiv_num:
			return maxdiv_num
		else:
			return maxdiv_den
