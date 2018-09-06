#Here this is my implementation of binary search

def bin_src(li, key):
	lo, hi = 0, len(li)-1
	
	while lo <= hi:
		mid = (lo + hi)//2
		if li[mid] == key:
			return 1
			
		if key < li[mid]:
			hi = mid-1
		else:
			lo = mid+1
	
	return -1
if __name__ == "__main__":
	li = [1]
	key = 1
	
	x = bin_src(li, key)
	
	if x == 1:
		print('found')
	else:
		print('Not found')
