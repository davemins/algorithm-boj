"""중앙 이동 알고리즘"""

'''
4 9 25 81 -> sq2 sq3 sq5 sq9 sq17
0일 때 2의 제곱
1일 때 2 + (2-1)의 제곱
2일 때 3 + (3-1)의 제곱

'''

process = int(input())

def side(process):
    if process == 1:
        return 3
    else:
        result = (2 * side(process - 1) - 1)
    return result

print(side(process) ** 2)