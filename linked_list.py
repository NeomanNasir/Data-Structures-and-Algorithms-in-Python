#A reverse list of Singly linked list is implemented by me
class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next
		
	def __repr__(self):
		return repr(self.data)
		
class LinkedList:
	def __init__(self):
		self.head = None
		
	def __repr__(self):
		nodes = []
		current_node = self.head
		
		while current_node:
			nodes.append(repr(current_node))
			current_node = current_node.next
			
		return ",".join(nodes)
		
	def prepend(self, data):
		node = Node(data, self.head)
		self.head = node
		
	def append(self, data):
		node = Node(data)
		
		if self.head is None:
			self.head = node 
			return
			
		current_node = self.head
		while current_node.next:
			current_node = current_node.next
			
		current_node.next = node
		
	def search(self, item):
		current_node = self.head
		
		while current_node:
			if current_node.data == item:
				return current_node
			
			current_node = current_node.next
			
		return None
		
	def remove(self, item):
		current_node = self.head #root node
		previous_node = None
		
		while current_node.data is not item:
			previous_node = current_node
			
			current_node = current_node.next
			
		if current_node == self.head:
			newnode = self.head
			self.head = newnode.next
		else:
			previous_node.next = current_node.next
			
	def insert(self, data, new_data):
		current_node = self.head
		
		while current_node.data is not data:
			
			current_node = current_node.next
			
		new_node = Node(new_data, current_node.next)
		current_node.next = new_node
		
	def reverse(self): 
		current_node = self.head
		prev_node = None
		while current_node:
			if prev_node:
				next = current_node.next
				current_node.next = prev_node
			else:
				next = current_node.next
				current_node.next = None
				
			prev_node = current_node
			current_node = next
			
		self.head = prev_node
			
if __name__ == "__main__":
	LL = LinkedList()
	LL.append(4)
	LL.append(5)
	LL.append(-1)
	LL.append(3)
	LL.append(0)
	
	print("Given LL: ", LL)
	LL.reverse()
	print("Reverse LL: ", LL)
		
		
				
