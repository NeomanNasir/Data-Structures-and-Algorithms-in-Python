#here we give priority to min element
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
		
def extract_min(heap):
	heap_size = len(heap)-1
	min_item = heap[1]
	heap[1] = heap[heap_size]
	min_heapify(heap, heap_size-1, 1)
	del heap[heap_size]
	return min_item
	
def insert_node(heap, node):
	heap_size = len(heap)-1
	heap.append(node)
	i = heap_size+1
	
	while i > 1 and heap[i] < heap[parent(i)]:
		heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
		i = parent(i)
		
def increase_key(heap, i, new_value):
	heap[i] = new_value #new value must be smaller than heap[i]
	
	while i > 1 and heap[i] < heap[parent(i)]:
		heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
		i = parent(i)
		
if __name__ == "__main__":
	H = [None, 1, 2, 6, 3, 5, 7, 9, 4, 9]
	print(H)
	print(extract_min(H), H)
	increase_key(H, 2, 0)
	print('After increasing value of 2nd element  :', H)
	

