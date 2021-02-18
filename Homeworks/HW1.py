matris = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print("List" + "\n")
print(matris)
print("-----------------" + "\n")

sayac = 0
start= 0
end = 50
while sayac < 3:
    temp = []
    breakLoop = 0

    for i in range(start, end):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
        	breakLoop += 1
        	if breakLoop < 4:
            		temp.append(i)
            		start = i+1

    matris[sayac] = temp
    sayac += 1

print("New List" + "\n")

print(matris)
