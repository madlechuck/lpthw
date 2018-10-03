def factorial(n):
	if n == 0:
		return 1
	num = 1
	while n >= 1:
		num = num * n
		n = n - 1
	return num		
	

print factorial(int(raw_input(">Print factorial of number:")))



