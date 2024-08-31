"""세탁소 사장 동혁"""

# 쿼터 0.25, 다임 0.10, 니켈 0.05, 페니 0.01

testcase = int(input())
tc_result = [[] for i in range(testcase)]

for i in range(testcase):
    money = int(input())
    Q = money // 25
    tc_result[i].append(Q)
    money -= Q * 25

    D = money // 10
    tc_result[i].append(D)
    money -= D * 10

    N = money // 5
    tc_result[i].append(N)
    money -= N * 5

    P = money // 1
    tc_result[i].append(P)

for j in tc_result:
    for m in range(4):
        print(j[m], end=' ')
    print()