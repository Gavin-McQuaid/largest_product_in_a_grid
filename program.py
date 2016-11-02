with open('grid.txt','r') as f:
	lines = []
	for line in f:
		lines.append(line.split())
	
	def down():
		i = 0
		while i < len(lines)-3:
			total = 0
			j = 0
			while j < 20:
				
				first,second,third,fourth = int(lines[i][j]), int(lines[i+1][j]), int(lines[i+2][j]),int(lines[i+3][j])
				if (first * second * third * fourth) > total:
					total = first * second * third * fourth
				j += 1

			i += 1
			return total
	def right():
		i = 0
		while i < 20 :
			total = 0
			j = 0
			while j < len(lines)-3:
				first,second,third,fourth = int(lines[i][j]), int(lines[i][j+1]), int(lines[i][j+2]),int(lines[i][j+3])
				if (first * second * third * fourth) > total:
					total = first * second * third * fourth
				j += 1

			i += 1
		return total
	def right_diagonal():
		total = 0
		i = 0
		while i < len(lines[i])-3:
			j = 0
			while j < len(lines)-3:
				first,second,third,fourth = int(lines[i][j]), int(lines[i+1][j+1]), int(lines[i+2][j+2]),int(lines[i+3][j+3])
				if (first * second * third * fourth) > total:
					total = first * second * third * fourth
				j += 1
		

			i += 1
			return total
	def left_diagonal():
		total = 0
		i = 3
		while i < len(lines[i])-3:
			j = 0
			while j < len(lines):
				first,second,third,fourth = int(lines[i][j]), int(lines[i+1][j-1]), int(lines[i+2][j-2]),int(lines[i+3][j-3])
				if (first * second * third * fourth) > total:
					total = first * second * third * fourth
				j += 1

			i += 1
		return total

print(down())
print(right())
print(right_diagonal())
print(left_diagonal())


