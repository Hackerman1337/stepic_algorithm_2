class Queue():	#O(n*m)
	def __init__(self):
		self.items = []
		self.items_length = 0
		self.max_elements = []

	def enqueue(self, item):
		self.items.insert(0,item)
		self.items_length += 1

	def dequeue(self):
		self.items.pop()
		self.items_length -= 1

	def main(self):
		n = int(input())
		arr = [int(i) for i in input().split()]
		m = int(input())

		for i in range(0, len(arr)):
			if self.items_length < m - 1:
				self.enqueue(arr[i])
			else:
				self.enqueue(arr[i])
				self.max_elements.append(max(self.items))
				self.dequeue()

		for i in self.max_elements:
			print(i, end=" ")
		print()

class New_Queue():	#O(n)
	def __init__(self):
		self.left_stack = []
		self.right_stack = []
		self.right_stack_max = []
		self.max_elements = []

	def enqueue(self, item):
		if len(self.left_stack) == 0:
			self.left_max = item
		else:
			if item > self.left_max:
				self.left_max = item
		self.left_stack.append(item)

	def dequeue(self):
		if len(self.right_stack) == 0:
			for i in range(len(self.left_stack) - 1, -1, -1):
				self.right_stack.append(self.left_stack[i])
				self.right_max(self.left_stack[i])
			self.left_stack = []

		if self.left_max > self.right_stack_max[-1]:
			self.max_elements.append(self.left_max)
		else:
			self.max_elements.append(self.right_stack_max[-1])
		self.right_stack.pop()
		self.right_stack_max.pop()

	def right_max(self, item):
		if len(self.right_stack_max) == 0:
			self.right_stack_max.append(item)
		else:
			if item > self.right_stack_max[-1]:
				self.right_stack_max.append(item)
			elif item <= self.right_stack_max[-1]:
				self.right_stack_max.append(self.right_stack_max[-1])

	def main(self):
		n = int(input())
		arr = [int(i) for i in input().split()]
		m = int(input())
		self.left_max = arr[0]

		for i in range(0, len(arr)):
			if len(self.left_stack) + len(self.right_stack) < m - 1:
				self.enqueue(arr[i])
			else:
				self.enqueue(arr[i])
				self.dequeue()

		for i in self.max_elements:
			print(i, end=" ")
		print()

test_obj = New_Queue().main()