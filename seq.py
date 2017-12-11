def printArray(arr, size):
	i=0
	while i<size:
		print(arr[i], end='')
		i+=1
	print(', ',end='')
	return

def recurnum(arr,m,n,place):
	if n==0:
		printArray(arr,place)	#,Function to print the elements
	if n>0:
		num=0
		while num<=m:
			arr.insert(place,num)	#,Inserting m in array
			recurnum(arr, m, n-1, place+1)
			num+=1
	return
	
def calculate(m,n):
	arr=[]			#,Initializing the list
	recurnum(arr,m,n,0)	#,0 is the index value
	return
	

m=int(input('Enter the value of m(value): '))
n=int(input('Enter the value of n(length): '))
if not m<=n:		#,To satisfy the given condition
	print('\nEnter the value such that n<=m')
	exit()
calculate(m,n)		#,A function to call a recursive function to print the list
