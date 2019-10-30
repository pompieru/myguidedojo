def sum_of_divs(n):
    sum = 0
    for i in range(1 , n//2+1):
        if n % i == 0:
          sum = sum+i
    return sum

def isPerfect(n):
    if sum_of_divs(n) ==n:
        return 1
    else:
        return 0

list_of_perfect_num = []
for i in range(1, 1001):
    if isPerfect(i) ==1:
        list_of_perfect_num.append(i)

print(list_of_perfect_num)
