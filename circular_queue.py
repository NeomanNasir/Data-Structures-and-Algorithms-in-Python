class Queue:
	#My implementation of circular queue
	def __init__(self, size):
		self.items = [0]*size
		self.max_size = size
		self.head, self.tail = -1, -1
		
	def enqueue(self, item):
		if (self.tail+1)%self.max_size == self.head:
			print("Queue is now Full!")
			return
		
		if self.tail == -1:
			self.head = 0
			self.tail = 0
			self.items[self.tail] = item
		else:
			self.tail = (self.tail + 1) % self.max_size
			self.items[self.tail] = item
		
	def dequeue(self):
		if self.head == -1:
			print("Queue is now Empty!")
			return None
		
		if self.head == self.tail:
			item = self.items[self.head]
			self.head = -1
			self.tail = -1
			return item
		else:
			item = self.items[self.head]
			self.head = (self.head + 1) % self.max_size
			return item
			
		
		
	def show_Queue(self):
		print(self.items)
		
	def is_empty(self):
		if self.head == -1:
			return True
		return False
		
if __name__ == "__main__":
	q = Queue(3)
	q.enqueue(10)
	q.enqueue(20)
	q.enqueue(30)
	q.enqueue(40)
	q.show_Queue()
	while not q.is_empty():
		print(q.dequeue())
	q.enqueue(40)
	print(q.dequeue())
	
		
			
	
