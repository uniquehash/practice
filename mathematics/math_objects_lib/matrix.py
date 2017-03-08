
from fractions import Fraction as ff


class Matrix(object):

	def __init__(self, array2d):
		self.x = array2d
		self.len = len(array2d)
		self.ident = Matrix.identity(array2d)
		self.stable_len = self.terminals_len()

	def __str__(self):
		return self.to_str()	

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



	def subset(self, rs, rf, cs, cf):
		col = range(cs, cf)
		row = range(rs, rf)

		sub = []
		tmp = []
		for j, e in enumerate(self.x):
			if j in row:
				tmp = []
				for i, x in enumerate(e):
					if i in col:
						tmp.append(x)
				sub.append(tmp)
		return sub

	@classmethod
	def identity(cls, trix):
		ident = []
		size = len(trix)
		for x in range(size):
			tmp = [0] * size
			tmp[x] = 1
			ident.append(tmp)

		return ident




	@classmethod
	def subtract(cls, trix0, trix1):
		matrix = []
		if len(trix0) != len(trix1):
			return []
		for i, y in enumerate(trix0):
			row = []
			for j, x in enumerate(y):
				row.append(trix0[i][j] - trix1[i][j])
			matrix.append(row)
		return matrix

	@classmethod
	def multiplaction(cls, trix0, trix1):
		rc_0 = Matrix.row_col_len(trix0)
		rc_1 = Matrix.row_col_len(trix1)

		if rc_0[1] != rc_1[0]:
			return []
		
		nm = []
		for i, y in enumerate(trix0):
			row = Matrix.dot_product(trix0, trix1, i, rc_1[1])
			nm.append(row)
		return nm


	@classmethod
	def row_col_len(cls, trix):
		row = len(trix)
		col = 0
		for x in trix[0]:
			col += 1			
		return (row, col)	

	@classmethod
	def dot_product(cls, trix0, trix1, row, col1):
		new_row = []		
		colum = 0
		for x in range(col1):
			dot_prod = 0
			col = 0
			for y in trix1:
				dot_prod += y[colum] * trix0[row][col]
				col += 1
			colum += 1
			new_row.append(dot_prod)
		return new_row

	@classmethod
	def inverse(cls, trix):
		size = len(trix)
		Matrix.inverse_form(trix)

		for x in range(size):
			if trix[x][x] != 1:
				trix[x] = Matrix.row_scale(trix[x], 1 / trix[x][x])
			for y in range(size):
				if y != x and trix[y][x] != 0:
					trix[y] = Matrix.row_subtract(trix[y], trix[x], trix[y][x])

		return Matrix.extract_inverse(trix, size)
		

	@classmethod
	def row_subtract(cls, row0, row1, scale):
		new_row = []
		for i in range(len(row0)):
			new_row.append(row0[i] - (row1[i] * scale))
		return new_row

	@classmethod
	def row_scale(cls, row, scale):
		new_row = []
		for e in row:
			new_row.append(e * scale)
		return new_row

	@classmethod
	def inverse_form(cls, trix):
		ident = Matrix.identity(trix)
		for i, e in enumerate(trix):
			trix[i] += ident[i]

	@classmethod
	def extract_inverse(cls, trix, size):
		for y in range(size):
			tmp = []
			for x in range(len(trix[y])):
				if x >= size:
					tmp.append(trix[y][x])
			trix[y] = tmp
		

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

















