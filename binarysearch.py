def binarysearch(inputlist, target):
	"""
	binary search for a target in a sorted list
	function returns True if target is in the list, False otherwise

	Input:
		inputlist: list
			the sorted list to be searched through
		target: int, float
			the target item to search for
	
	Return:
		True or False
	"""

	listlen = len(inputlist)
	if listlen==0:                  # if list is empty, search is done
		return False
	mididx = (len(inputlist))//2    # index of the middle item
	midval = inputlist[mididx]      # value of the middle item
	
	if midval==target:
		return True
	else:
		if midval>target:
			return binarysearch(inputlist[:mididx], target)
		else:
			return binarysearch(inputlist[mididx+1:], target)