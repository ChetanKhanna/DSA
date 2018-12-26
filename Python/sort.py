def Bubble_Sort(iterator):
	l = len(iterator)
	for i in range(l):
		for j in range(l-1):
			if iterator[j] > iterator[j+1]:
				temp = iterator[j]
				iterator[j] = iterator[j+1]
				iterator[j+1] = temp

def Selection_Sort(iterator):
	l = len(iterator)
	for i in range(l-1):
		mpos = i;
		for j in range(i+1, l):
			if iterator[j] < iterator[mpos]:
				mpos = j

		temp = iterator[i]
		iterator[i] = iterator[mpos]
		iterator[mpos] = temp

def Insertion_Sort(iterator):
	l = len(iterator)
	for i in range(1, l):
		val = iterator[i]
		j = i
		while j > 0 and iterator[j-1] > val:
			iterator[j] = iterator[j-1]
			j = j - 1
		iterator[j] = val

def Shell_Sort(iterator):
	l = len(iterator)
	gap = l/2
	while gap > 0:
		for i in range(gap, l):
			val = iterator[i]
			j = i
			while j > 0 and iterator[j-1] > val:
				iterator[j-1] = iterator[j]
				j = j - 1
			iterator[j] = val
		gap = gap / 2

def Merge_Sort(iterator):
	if len(iterator)>1:
		mid = len(iterator)//2
		left = iterator[:mid]
		right = iterator[mid:]

		Merge_Sort(left)
		Merge_Sort(right)

		i,j,k = 0,0,0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				iterator[k] = left[i]
				i = i + 1
			else:
				iterator[k] = right[j]
				j = j + 1
			k = k + 1

		while i < len(left):
			iterator[k] = left[i]
			i = i + 1
			k = k + 1

		while j < len(right):
			iterator[k] = right[j]
			j = j + 1
			k = k + 1

def Quick_Sort(iterator):
	Quick_Sort_helper(iterator,0,len(iterator)-1)

def Quick_Sort_helper(iterator, first, last):
	if first < last:
		splitpoint = partition(iterator, first, last)

		Quick_Sort_helper(iterator, first, splitpoint-1)
		Quick_Sort_helper(iterator, splitpoint+1, last)

def partition(iterator, first, last):
	pivotValue = iterator[first]

	left =first + 1
	right = last

	done = False
	while not done:
		while left <= right and iterator[left] <= pivotValue:
			left = left + 1

		while right >= left and iterator[right] >= pivotValue :
			right = right - 1

		if left > right:
			done = True
		else:
			temp = iterator[left]
			iterator[left] = iterator[right]
			iterator[right] = temp

	temp = iterator[first]
	iterator[first] = iterator[right]
	iterator[right] = temp

	return right