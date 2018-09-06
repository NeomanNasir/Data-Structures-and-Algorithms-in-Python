#implementation of Binary search tree
#left child is less than root node and right child is greater.

class Node:
	def __init__(self, data):
		self.data = data
		self.parent = None
		self.left = None
		self.right = None
		
	def __repr__(self):
		return repr(self.data)
		
	def add_left(self, node):
		self.left = node
		if node is not None:
			node.parent = self
			
	def add_right(self, node):
		self.right = node
		if node is not None:
			node.parent = self
	
def insert_node(root, node):
	current_node = root
	last_node = None
	
	while current_node:
		last_node = current_node
		if node.data < current_node.data:
			current_node = current_node.left
		else:
			current_node = current_node.right
			
	if node.data < last_node.data:
		last_node.add_left(node)
	else:
		last_node.add_right(node)
		
def in_order(node): #sorted
	#left -> root -> right
	
	if node.left:
		in_order(node.left)
	print(node)
	if node.right:
		in_order(node.right)
		
def search(root, key):
	current_node = root
	while current_node:
		if current_node.data == key:
			return current_node
		elif key < current_node.data:
			current_node = current_node.left
		else:
			current_node = current_node.right
			
	return None
	
def remove(root, key):
	node = search(root, key)
	x = node
	if node.left is None and node.right is None:
		node = None
	elif node.left is None:
		node.parent.add_left(node.right)
		if x == root:
			root = node
	elif node.right is None:
		node.parent.add_right(node.left)
		if x == root:
			root = node
	else:
		current_node = node.right
		while current_node:
			successor = current_node
			current_node = current_node.left
		node.data = successor.data

		if successor.right:
			successor.parent.add_left(successor.right)
		else:
			successor.parent.add_right(None)
			
	return root
		
if __name__ == "__main__":
	root = Node(10)
	
	for item in [5, 17, 3, 7, 12, 19, 1, 4]:
		node = Node(item)
		insert_node(root, node)
		
	node = Node(13)
	insert_node(root, node)
		
	print(root)
	print("tree element in sorted:")
	in_order(root)
	print("searching.......")
	x = search(root, 5)
	if x is not None:
		print(x, 'is found!')
	else:
		print('not found!')
		
	print("removing.... 5")
	root = remove(root, 5)
	print(root)
	print("tree element in sorted:")
	in_order(root)
		
	

