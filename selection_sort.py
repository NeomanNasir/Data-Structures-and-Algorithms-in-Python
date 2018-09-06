#My implementation of selection sort
#Every step of the list, we have to find the smallest number and put it first sequencially
def selection_sort(li):
	length = len(li)-1
	for i in range(length): #i will go up to length-1
		for j in range(i+1, length+1):
			if li[i] > li[j]:
				li[i], li[j] = li[j], li[i] 
		

if __name__ == "__main__":
	#li = [2, -1, 3, 4, 3, -1]
	li = [5, 4, 3, 2, 1]
	
	selection_sort(li)
	
	print(li)
