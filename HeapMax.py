# A complete binary tree
# childs are alaways less than parent

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

def build_max_heap(binary_tree):
	n = len(binary_tree) - 1
	for i in range(n//2, 0, -1):
		max_heapify(binary_tree, n, i)
		
def heap_sort(heap):
	#Time Complexity O(nlogn)
	build_max_heap(heap)
	heap_size = len(heap) - 1
	
	for i in range(heap_size, 1, -1):
		#print(i)
		heap[1], heap[i] = heap[i], heap[1]
		heap_size -= 1
		#print('- ', heap_size)
		max_heapify(heap, heap_size, 1)
	
	
if __name__ == "__main__":
	H = [None, 19, 7, 17, 3, 5, 12, 10, 1, 2]
	print(H, is_Max_Heap(H))
	H = [None, 19, 7, 12, 3, 5, 17, 10, 1, 2]
	print(H)
	max_heapify(H, len(H)-1, 3)
	print(H)
	H = [None, 12, 7, 1, 3, 10, 17, 19, 2, 5]
	print("Before building heap", H)
	build_max_heap(H)
	print("After Building heap", H)
	heap_sort(H)
	print("After sorting: ", H)

