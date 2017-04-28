import sys

sys.setrecursionlimit(20000)

def heigth_of_a_tree(vertex):
	height = 1
	if vertex in tops:
		for child in tops[vertex]:
			height = max(height, heigth_of_a_tree(child) + 1)
	return(height)

length = input()
tree = [int(i) for i in input().split()]

tops = {}

for i in range(len(tree)):
	if tree[i] == -1:
		vertex = i
	else:
		if tree[i] not in tops:
			tops[tree[i]] = [i]
		else:
			tops[tree[i]] += [i]

print(heigth_of_a_tree(vertex))