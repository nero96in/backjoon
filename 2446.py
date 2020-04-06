N = int(input())
size = 2*N-1
for i in range(N): print(" "*i+"*"*(size-2*i))
for j in range(N-2, -1, -1): print(" "*j+"*"*(size-2*j))