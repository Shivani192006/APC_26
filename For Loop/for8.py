# Write a PYTHON program to produce following design
			#A B C 
			#A B C 
			#A B C

for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()
