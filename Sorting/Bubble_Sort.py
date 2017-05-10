def bubblesort(array): 
	swaps = True            ### Short Bubble: breaks if no swaps
	for i in range(len(array)):
		swaps = False
		for x in range(len(array)-i-1):
			if array[x+1]<array[x]:
				swaps = True
				temp = array[x+1]
				array[x+1] = array[x]
				array[x] = temp
	return array