#My implementation of bubble sort

#Here we compare to corresponding two element of the list and put smallest first

def bubble_sort(li):
	length = len(li)
	for i in range(length):
		for j in range(length-i-1): #with every step of first loop the greatest elements are stores in right side of list. so we can ingnore.
			if li[j] > li[j+1]:
				li[j], li[j+1] = li[j+1], li[j]
		

if __name__ == "__main__":
	li = [2, -1, 3, 4, 3, -1]
	#li = [5, 4, 3, 2, 1]
	
	bubble_sort(li)
	
	print(li)
