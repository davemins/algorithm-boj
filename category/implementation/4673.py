'''
# 문제 이해
셀프 넘버를 구하려고 한다.

# 발상
완전 탐색 문제인데 리스트에서 조건에 맞지 않는 것을 빼면서 구하려 한다.

# 복잡도
while문이 있기에 어마어마하다.

'''
numbers = [i for i in range(1, 10001)]

def function(k):
    data = str(k)
    result = k
    for i in range(len(data)):
        result += int(data[i])
    return result

for i in range(1, 10000):
    if i in numbers:
        k = i
        while k <= 10000:
            k = function(k)
            if k in numbers:
                numbers.remove(k)
            else:
                break

for j in range(len(numbers)):
    print(numbers[j], end='\n')
'''
# 푼 시간
26분

# 채점
정답

# 느낀 점
처음에는 시간 초과가 났었다.
하지만 문제를 다시 읽고 break문을 추가하여 맞출 수 있었다.
정말 짜릿하다.
잘 안되는 부분이 있으면 다시 문제를 읽어보자.
'''