





class Matrix(object):

	def __init__(self, array2d):
		self.x = array2d
		self.len = len(array2d)
		self.ident = self.identity()


	def __str__(self):
		s = ""
		s += "[\n"
		for x in self.x:
			s += "  ["
			s += "  "
			for y in x:		
				s += str(y)
				s += ", "
			s += "],\n"
		s += "]"
		return s	

	def identity(self):
		top = [] 				
		
		for x in range(self.len):
			arr = []			
			tmp = [0] * self.len
			tmp[x] = 1
			top.append(tmp)

		return top
























