# #1 거스름돈
cost = [500, 100, 50, 10]
cnt = [0, 0, 0, 0]
N = int(input())
for i in range(4):
    cnt[i] = N // cost[i]
    N %= cost[i]
for _ in range(4):
    print(str(cost[_])+"원짜리 동전: "+str(cnt[_])+"개")
