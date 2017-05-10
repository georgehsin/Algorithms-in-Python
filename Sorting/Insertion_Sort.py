def insertionsort(array):
	for x in range (1, len(array)):
		current = array[x]
		i = x
		while i > 0:
			if current < array[i-1]:
				array[i] = array[i-1]
				i -=1
			else:
				break
		array[i]=current
	return array