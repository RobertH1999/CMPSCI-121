def linearSearch(item, dataList):
	for i in range(len(datalist):
		if dataList[i] == item:
			return True
		return False
				   
def binarySearch(item, dataList):				   
	if len(dataList) == 0:
		return False
	else:
		midpoint = len(dataList)//2
	if dataList[midpoint] == item:
		return True
	else:
		if item < dataList[midpoint]:
			return binarySearch(item, dataList[:midpoint])
		else:
			return binarySearch(item,dataList[midpoint + 1:])
             
                   
				   
