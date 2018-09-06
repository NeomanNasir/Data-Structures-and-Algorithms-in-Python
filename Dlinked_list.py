#implementation of Doubly Linked list
class Node:
	def __init__(self, data=None, prev=None, next=None):
		self.data = data
		self.prev = prev
		self.next = next
		
	def __repr__(self):
		return repr(self.data)
		
class DLinkedList:
	def __init__(self):
		self.head = None #root node
	
	def __repr__(self):
		nodes = []
		current_node =self.head
		
		while current_node:
			nodes.append(repr(current_node))
			current_node = current_node.next
			
		return ','.join(nodes)
		
	def prepend(self, data):
		node = Node(data, next=self.head)
		if self.head:
			self.head.prev = node
		self.head = node
		
	def append(self, data):
		
		if self.head == None:
			self.head = Node(data)
			return
		
		current_node = self.head
		while current_node.next:
			current_node = current_node.next
			
		new_node = Node(data, prev=current_node)
		current_node.next = new_node
		
	def search(self, item):
		current_node = self.head
		while current_node:
			if current_node.data == item:
				return current_node
			
			current_node = current_node.next
			
		return None
	
	def remove(self, item):
		current_node = self.head
		
		while current_node.data is not item:
			current_node = current_node.next
		
		if current_node== self.head:
			node = self.head
			self.head = node.next
			if self.head:
				self.head.prev = None
		else:
			current_node.prev.next = current_node.next
			if current_node.next:
				current_node.next.prev = current_node.prev
				
	def insert(self, data, new_data): #insert new_data after data
		current_node = self.search(data)
		
		if current_node is None:
			return
		new_node = Node(new_data, current_node, current_node.next)
		current_node.next = new_node
		
		
	
	
