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
def insertionSort(dataList):
	for index in range(len(dataList)):
		current = dataList[index]
		position = index
            
        while position > 0 and dataList[position - 1] > current:
			dataList[position] = dataList[position - 1] 
			position -= 1
		dataList[position] = current
	return dataList
		
				   
				   
				   
				   
				   
				   
