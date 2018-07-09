#构造自己的序列
def checkIndex(key):
	"""
		所给的键是能接受的索引吗？

		键应该是一个非负的整数
		如果是负数引发IndexErorr
		如果不是整数引发TypeError
		"""
	if not isinstance(key,(int)) : raise TypeError
	if key < 0 : raise IndexError

class ArithmeticSequence:
	def __init__(self,start=0,step=1):
		"""
			初始化算术序列
			起始值
			步长
			改变
			"""
		self.start = start
		self.step = step
		self.changed={}

	def __getitem__(self,key):
		"""
			Get an item from the arithmetic sequence.
		"""
		checkIndex(key)

		try:
			return self.changed[key]
		except KeyError:
			return self.start + key*self.step

	def __setitem__(self,key,value):
		"""
		修改算术序列的像
		"""
		checkIndex(key)

		self.changed[key] = value

	def __len__(self):
		return len(self.changed)

s = ArithmeticSequence(1,2)
s[4]
print(s[7])