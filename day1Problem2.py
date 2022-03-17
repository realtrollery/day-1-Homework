# #2 대학생 기업 코딩 테스트 기출문제
N, K = map(int, input().split())
step = 0
while N != 1:
    if N % K == 0:
        N//=K
    else:
        N -= 1
    step += 1
print(step)
