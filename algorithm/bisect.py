#二分查找
def search(sequence,number,lower=0,upper=None):
	
	if upper is None:upper = len(sequence)-1
	if lower == upper:
		assert number == sequence[upper]
		return upper
	else:
		middle = (upper + lower) // 2
		print(lower,upper,middle)
		if number > sequence[middle]:
			return search(sequence,number,middle+1,upper)
		else:
			return search(sequence,number,lower,middle)

seq = [23,24,124,56,11,131]
seq.sort()
print(seq)
print(search(seq,124))