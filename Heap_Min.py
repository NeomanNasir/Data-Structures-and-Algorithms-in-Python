# childs must be greater than their parent

def left(i):
	return i * 2
	
def right(i):
	return i*2 + 1
	
def parent(i):
	return i // 2
	
def is_Min_Heap(heap):
	heap_size = len(heap) - 1
	for i in range(heap_size, 1, -1):
		if heap[parent(i)] > heap[i]:
			return False
		
	return True

def min_heapify(heap, heap_size, i):
	#take i as a parent node and make the subtree min heap
	#make sure that subtree of childs(if have) are min heap
	l = left(i)
	r = right(i)
	
	if l <= heap_size and heap[l] < heap[i]:
		lowest = l
	else:
		lowest = i
		
	if r <= heap_size and heap[r] < heap[lowest]:
		lowest = r
		
	if lowest != i:
		heap[i], heap[lowest] = heap[lowest], heap[i]
		min_heapify(heap, heap_size, lowest)	
def build_min_heap(heap):
	heap_size = len(heap) - 1
	
	for i in range(heap_size//2, 0, -1): #looping that nodes that has one or more subtree
		min_heapify(heap, heap_size, i)
		
def heap_sort(heap):
	#greater to smaller
	build_min_heap(heap)
	heap_size = len(heap) - 1
	
	for i in range(heap_size, 1, -1):
		heap[i], heap[1] = heap[1], heap[i]
		heap_size -= 1
		min_heapify(heap, heap_size, 1)
		
def insert_node(heap, node):
	heap_size = len(heap)-1
	heap.append(node)
	i = heap_size+1
	
	while i > 1 and heap[i] < heap[parent(i)]:
		heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
		i = parent(i)
	
if __name__ == "__main__":
	H = [None, 9, 3, 2, 4, 5, 7, 6, 1, 9]
	print(H, is_Min_Heap(H))
	min_heapify(H, 9, 1)
	print(H)
	build_min_heap(H)
	print('After building min heap: ', H)
	heap_sort(H)
	print('After sorting: ', H)
	
