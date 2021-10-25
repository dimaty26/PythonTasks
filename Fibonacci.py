def fibonacci(n):
	if n == 1:
		return 0
	if n == 2:
		return 1

	return fibonacci(n - 1) + fibonacci(n - 2)

a = fibonacci(5)
b = fibonacci(4)
c = fibonacci(3)
d = fibonacci(2)
e = fibonacci(1)

print(a)
print(b)
print(c)
print(d)
print(e)
print(fibonacci(9))