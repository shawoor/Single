def printArray(arr, size):
	i=0
	while i<size:
		print(arr[i], end='')
		i+=1
	print(', ',end='')
	return

def recurnum(arr,m,n,place):
	if n==0:
		printArray(arr,place)
	if n>0:
		num=0
		while num<=m:
			arr.insert(place,num)
			recurnum(arr, m, n-1, place+1)
			num+=1
	return
	
def calculate(m,n):
	arr=[]
	recurnum(arr,m,n,0)
	return
	

m=int(input('Enter the value of m(value): '))
n=int(input('Enter the value of n(length): '))
if not n<=m:
	print('\nEnter the value such that n<=m')
	exit()
calculate(m,n)