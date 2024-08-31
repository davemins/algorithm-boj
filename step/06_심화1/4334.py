"""평균은 넘겠지"""

test_case = int(input())

student = []
score = [[] for _ in range(test_case)]

for i in range(test_case):
    case = input()
    bag = list(map(int, case.split()))
    student.append(bag[0])
    for j in range(1, bag[0] + 1):
        score[i].append(bag[j])

for m in range(len(student)):
    average = sum(score[m])/ student[m]
    count = 0
    for n in score[m]:
        if n > average:
            count += 1
    ratio = "{:.3f}".format(count / student[m] * 100)
    print(ratio + '%')