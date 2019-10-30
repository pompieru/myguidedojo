doors = [0]*100
for i in range (1, 101):
    for j in range (i-1,100,i):
        if doors[j]== 0:
            doors[j] = 1
        elif doors[j]==1:
            doors[j] = 0
opendoors = []
for i, value in enumerate(doors):
    if value == 1:
        opendoors.append(i+1)
print('the following doors are open: ', opendoors)