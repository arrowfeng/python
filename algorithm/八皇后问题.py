
import random
#state[0]=1表示是在第1行第2列已经有皇后了
def conflict(state,nextX):
	nextY = len(state)#行
	for i in range(nextY):#遍历每一行
		if abs(state[i]-nextX) in (0,nextY-i):#横竖或对角上不能存在其他皇后
			return True
	return False

def queens(num=8, state=()):
	for pos in range(num):
		if not conflict(state,pos):
			if len(state) == num - 1:
				yield (pos,)
			else:
				for result in queens(num, state + (pos,)):
					yield (pos,) + result

#打印助手函数
def prettyprint(solution):
	def line(pos,length=len(solution)):
		return '.'*(pos) + 'X' +'.'*(length-pos-1)
	for pos in solution:
		print(line(pos))

prettyprint(random.choice(list(queens(8))))