
from fractions import Fraction as ff


class Matrix(object):

	def __init__(self, array2d):
		self.x = array2d
		self.len = len(array2d)
		self.ident = self.identity()
		self.stable_len = self.terminals_len()

	def __str__(self):
		return self.to_str()

	def identity(self):
		top = [] 				
		
		for x in range(self.len):
			arr = []			
			tmp = [0] * self.len
			tmp[x] = 1
			top.append(tmp)

		return top

	def to_str(self, arr=None):
		s = ""
		s += "[\n"

		count = 0
		if not arr:
			arr = self.x

		for x in arr:
			s += "  ["
			s += "  "
			for y in x:		
				s += str(y)
				s += ", " 				
			s += "], "+ str(count)+"\n"
			count += 1
		s += "]"
		return s


	def canonical_form(self):
		self.proper_order()
		self.proper_form()


	def proper_form(self):
		for i, e in enumerate(self.x):
			if e == [0] * self.len:
				self.x[i][i] = 1
			else:
				self.fractionize(i)

	def proper_order(self):		
		while not self.verify_form():
			index = self.index_to_push()
			self.shift_right(index)
			self.push_down_row(index)

	def fractionize(self, index):
		total = 0
		for e in self.x[index]:
			total += e
		for i, e in enumerate(self.x[index]):
			self.x[index][i] = ff(e, total)

	def index_to_push(self):
		well_formed = True
		for i, e in enumerate(reversed(self.x)):			
			if e != [0] * self.len:			
				well_formed = False
			if e == [0] * self.len and well_formed == False:				
				return (self.len - i - 1)

	def shift_right(self, index):		
		for e in self.x:
			tmp = e[index + 1]
			e[index + 1] = e[index]
			e[index] = tmp

	def push_down_row(self, index):
		tmp = self.x[index+1]
		self.x[index+1] = self.x[index]
		self.x[index] = tmp

	def verify_form(self):		
		arr = self.x[self.len - self.stable_len:]
		count = 0		
		for e in arr:
			if e == [0] * self.len:
				count += 1
		if count == self.stable_len:
			return True
		else:
			return False


	def terminals_len(self):
		stable = 0
		for e in self.x:
			if e == [0] * self.len:
				stable += 1
		return stable

















