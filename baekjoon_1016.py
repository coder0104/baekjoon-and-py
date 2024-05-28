min, max = map(int, input().split())

answer = max - min + 1
squ = [False] * (max-min+1)

for i in range(2, int(max**0.5+1)):
    square = i**2
    for j in range((((min-1)//square)+1)*square, max+1, square):
        if not squ[j-min] :
            squ[j-min] = True
            answer -= 1
print(answer)