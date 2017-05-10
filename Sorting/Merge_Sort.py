def mergesort(array):
	if len(array) <= 1:
		return array
	else:
		mid = len(array)/2
		left = array[:mid]
		right = array[mid:]
		mergesort(left)
		mergesort(right)
		x = 0
		y = 0
		z = 0
		while x < len(left) and y <len(right):
			if left[x] < right[y]:
				array[z] = left[x]
				x += 1
			else:
				array[z] = right[y]
				y += 1
			z += 1

		while x < len(left): 
			array[z] = left[x]
			x += 1
			z += 1

		while y <len(right):
			array[z] = right[y]
			y += 1
			z += 1
	return array