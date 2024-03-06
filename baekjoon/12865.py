import sys

numbers = []
CNT, W = map(int, sys.stdin.readline().split())

for line in sys.stdin:
    things = line.strip().split()
    things = [int(thing) for thing in things]
    
    numbers.append(tuple(things))

# dp = []
# for _ in range(CNT+1):
#     dp.append([0]*(W+1))
dp = [[0]*(W+1) for _ in range((CNT+1))]
#print(dp)

for i in range(1, CNT+1):
    for j in range(1, W+1):
        wght = numbers[i-1][0]
        val = numbers[i-1][1]
        
        if j < wght:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-wght] + val)

print(dp[CNT][W])