'''
def print_n(n):
	if n == 0:
		return
	
	print(n)
	print_n(n-1)
	print(n)
	
if __name__ == "__main__":
	print_n(5)
'''

#my implementation of binary search using recursion
def bin_src(li, key, lo, hi):
	mid = (lo+hi)//2
	if lo > hi:
		return -1
	elif li[mid] == key:
		return mid
		
	if key < li[mid]:
		return bin_src(li, key, lo, mid-1)
	else:
		return bin_src(li, key, mid+1, hi)
	
if __name__ == "__main__":
	li = [-1, 0, 2, 3, 4, 5]
	key = -1
	lo, hi = 0, len(li)-1
	x = bin_src(li, key, lo, hi)
	print(x)
	
	if x == -1:
		print('Not found')
	else:
		print('found')
		
		
		
		
