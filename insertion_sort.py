#My implementation of insertion sort
#by storing every list element sequencially, then check previous items if they are greater then have to change.

def insertion_sort(li):
	n = len(li)
	for i in range(1, n):
		j = i-1
		x = li[i]
		while li[j] > x and j >= 0:
			li[j+1] = li[j]
			j -= 1
			
		li[j+1] = x
		

if __name__ == "__main__":
	li = [2, -1, 3, 4, 3, -1]
	#li = [5, 4, 3, 2, 1]
	
	insertion_sort(li)
	
	print(li)
