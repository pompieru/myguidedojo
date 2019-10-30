x = [-5, 23, 0, -9, 12, 99, 105, -43]
max = min = x[0]
i = 1
n = len(x)
while i < n:
    if x[i] > max:
        max = x[i]
    if x[i] < min:
        min = x[i]
    i = i + 1
print(max,min)

sum = 0
for num in x:
    sum = sum + int(num)

print(sum/n)