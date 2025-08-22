N = int(input())
i = 2 # (2, N-1)
while i <= N-1:
    if N % i == 0:
        # composite number detected
        break
    i +=1
print("end")