# This program simulates dice rolls for the boardgame "Risk". Simply input the number of attack dice in the first line and the number of defence in the second.
from random import randint
atkno=int(input("number of attack dice: "))
print(atkno)
defno=int(input("number of defence dice: "))
print(defno)
print("attack dice:")
a1=randint(1,6)
a2=randint(1,6)
a3=randint(1,6)
d1=randint(1,6)
d2=randint(1,6)

if atkno==1:
	print(a1)
	atklist=[a1]
elif atkno==2:
	print(a1)
	print(a2)
	atklist=sorted([a1,a2])
elif atkno==3:
	print(a1)
	print(a2)
	print(a3)
	atklist=sorted([a1,a2,a3])
elif atkno>=4:
	print("you can not have more than 3 attack dice")

print("defence dice:")
if defno==1:
	print(d1)
	deflist=sorted([d1])
elif defno==2:
	print(d1)
	print(d2)
	deflist=sorted([d1,d2])
elif defno>=3:
	print("you cannot have more than 2 defence dice")

atkord=(atklist[::-1])
deford=(deflist[::-1])

if atkno==1:
	if deford[0] >= a1:
		print("attacker loses one army")
	else:
		print("defender loses one army")
elif defno==1:
	if d1 >= atkord[0]:
		print("attacker loses 1 army")
	else:
		print("defender loses 1 army")
elif defno==2:
	if deford[0]>=atkord[0]and deford[1]>=atkord[1]:
		print("attacker loses 2 armies")
	elif deford[0]<atkord[0] and deford[1]<atkord[1]:
		print("defender loses 2 armies")
	else:
		print("attacker and defender lose an army each")
