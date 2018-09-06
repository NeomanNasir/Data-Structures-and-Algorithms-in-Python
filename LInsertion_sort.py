#insertion sort implementation using linked list

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
		
	def append(self, data):
		
		if self.head == None:
			self.head = Node(data)
			return
		
		current_node = self.head
		while current_node.next:
			current_node = current_node.next
			
		new_node = Node(data, prev=current_node)
		current_node.next = new_node
		
		
	def insertion_sort(self):
		#My implementation of insertion_sort using linked_list
		#Worst case Time complexity as usual: O(n^2)
		#Memory complexity: O(1)
		next_node = self.head.next
		while next_node:
			current_data = next_node.data
			prev_node = next_node.prev
			while prev_node and prev_node.data > current_data:
				prev_node.next.data = prev_node.data
				prev_node = prev_node.prev
				
			if prev_node == None:
				self.head.data = current_data
			else:
				prev_node.next.data = current_data
			next_node = next_node.next
		
if __name__ == "__main__":
	LL = DLinkedList()
	LL.append(4)
	LL.append(5)
	LL.append(-1)
	LL.append(3)
	LL.append(0)
	
	print("Given Llist: ",LL)
	LL.insertion_sort()
	print("After sorting: ", LL)
	
	
		
