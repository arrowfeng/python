class CounterList(list):
	def __init__(self, *arg):
		super(CounterList, self).__init__(*arg)
		self.counter = 0

	def __getitem__(self,index):
		self.counter+=1
		return super(CounterList.self).__getitem__(index)
cl = CounterList(range(10))
print(cl)
