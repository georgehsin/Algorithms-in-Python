def binarySearch(val, arr):
	if len(arr)<1:
		return False
	l = 0
	r = len(arr)
	mid = len(arr)/2
	while r>=l:
		if arr[mid]==val:
			return mid
		elif arr[mid]>val:
			r = mid
			mid = l+(r-l)/2
		else:
			l = mid
			mid = mid+(r-l)/2
	return False