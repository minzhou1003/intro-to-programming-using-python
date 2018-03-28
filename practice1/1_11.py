# copyright minzhou@bu.edu


n = 5
p = 312032486

birth = 7
death = 13
imm = 45

one_year = 365 * 24 * 3600

for i in range(n):
	next_year = p + one_year // birth - one_year // death + one_year // imm
	print(next_year)
	p = next_year