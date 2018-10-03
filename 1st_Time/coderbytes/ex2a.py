def factorial(n):
	if n == 0:
		return 1
	mul = 1
	while n >= 1:
		mul = mul * n		
		n = n - 1
	return mul
print factorial(int(raw_input("enter number:"))) 