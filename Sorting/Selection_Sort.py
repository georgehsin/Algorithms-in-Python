def selectionsort(array):
	for x in range(len(array)):
		maxidx = i
		for i in range(0,len(array)-x):
			if array[i] > array[maxidx]:
				maxidx = i
		temp = array[maxidx]
		array[maxidx] = array[len(array)-x-1] 
		array[len(array)-x-1] = temp
	return array