string = input()
brackets = {"(": ")", "[": "]", "{": "}"}

def check(string, brackets, count=1):
	stack = []
	if len(string) > 1:
		for i in range(len(string)):
			if string[i] in brackets:
				stack.append({string[i] : count})
			elif string[i] in brackets.values():
				if len(stack) != 0:
					if brackets[stack[-1].popitem()[0]] != string[i]:
						return count
					else:
						stack.pop()
				else:
					return count
			count += 1
	else:
		return count
	if len(stack) > 0:
		return stack.pop().popitem()[1]
	else:
		return "Success"

print(check(string, brackets))