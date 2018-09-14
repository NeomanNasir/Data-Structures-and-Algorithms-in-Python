# implementation of Priority Queue using Max Heap
def left_index(i):
	return i * 2
	
def right_index(i):
	return i*2 + 1
	
def parent_index(i):
	return i // 2
	
def is_Max_Heap(H):
	n = len(H) - 1
	for i in range(n, 1, -1):
		x = parent_index(i)
		if H[x] < H[i]:
			return False
		
	return True
	
def max_heapify(heap, h_size, i):
	# take i as a root node and make it and all it's subtree max heap
	l = left_index(i)
	r = right_index(i)
	
	if l <= h_size and heap[l] > heap[i]:
		largest_i = l
	else:
		largest_i = i
		
	if r <= h_size and heap[r] > heap[largest_i]:
		largest_i = r
		
	if largest_i != i:
		heap[i], heap[largest_i] = heap[largest_i], heap[i]
		#print(heap)
		max_heapify(heap, h_size, largest_i)
		
def get_maximum(heap):
	return heap[1]
	
def extract_max(heap):
	heap_size = len(heap)-1
	max_item = heap[1]
	heap[1] = heap[heap_size]
	max_heapify(heap, heap_size-1, 1)
	del heap[heap_size]
	return max_item
	
def insert_node(heap, node):
	heap_size = len(heap)-1
	heap.append(node)
	i = heap_size+1
	
	while i > 1 and heap[i] > heap[parent_index(i)]:
		heap[parent_index(i)], heap[i] = heap[i], heap[parent_index(i)]
		i = parent_index(i)
		
def increase_key(heap, i, new_value):
	heap[i] = new_value #new value must be greater than heap[i]
	
	while i > 1 and heap[i] > heap[parent_index(i)]:
		heap[parent_index(i)], heap[i] = heap[i], heap[parent_index(i)]
		i = parent_index(i)
		
if __name__ == "__main__":
	H = [None, 19, 10, 17, 5, 7, 12, 1, 2, 3]
	print(len(H), extract_max(H), H, len(H))
	insert_node(H, 10)
	print(H, len(H))
	increase_key(H, 2, 20)
	print(H)
	

	
