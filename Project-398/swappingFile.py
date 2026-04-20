def swapFileData():
	file1=input()
	file2=input()
	with open(str(file1), 'r') as a:
		data_a=a.read()
	with open(str(file2), 'r') as a:
		data_b=a.read()
	with open(str(file1), 'w') as a:
		a.write(data_b)
	with open(str(file2), 'w') as a:
		a.write(data_a)
swapFileData()