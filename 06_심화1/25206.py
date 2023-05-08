"""너의 평점은"""

score_dic = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}

score_list = []
credit_list = []

for i in range(20):
    cource, credit, score = map(str, input().split())
    if score == "P":
        continue
    else:
        credit_list.append(float(credit))
        score_list.append(score_dic[score] * float(credit))

average = sum(score_list) / sum(credit_list)
print("{:.6f}".format(average, 6))