class Stack_max():
	def __init__(self):
		self.stack = []
		self.stack_max = []
		self.length = 0
		self.length_max = 0

	def push(self, numb):
		self.stack.append(numb)
		self.length += 1
		self.max()

	def pop(self):
		if self.length > 0:
			self.stack.pop()
			self.length -= 1
			self.stack_max.pop()
			self.length_max -= 1
		else:
			print("Error")

	def max(self, inp=0):
		if self.length > 0:
			if inp == 1:
				print(self.stack_max[-1])
			else:
				if self.length_max == 0:
					self.stack_max.append(self.stack[0])
					self.length_max += 1
				else:
					if self.stack[-1] > self.stack_max[-1]:
						self.stack_max.append(self.stack[-1])
						self.length_max += 1
					elif self.stack[-1] <= self.stack_max[-1]:
						self.stack_max.append(self.stack_max[-1])
						self.length_max += 1
		else:
			print("Error")

	def main(self):
		count = int(input())
		for i in range(count):
			method = [i for i in input().split()]
			if method[0] == "push":
				self.push(int(method[1]))
			elif method[0] == "pop":
				self.pop()
			elif method[0] == "max":
				self.max(inp=1)

test_obj = Stack_max().main()