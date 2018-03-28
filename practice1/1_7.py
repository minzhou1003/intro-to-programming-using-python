# copyright minzhou@bu.edu


n = 6
res = 1
for i in range(1, n):
	res += (-1) ** i * (1 / (2 * i + 1))
res = 4 * res
print(res)