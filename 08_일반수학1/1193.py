"""분수찾기"""

'''

1  1 2  3 2 1  1 2 3 4  5 4 3 2 1  

1  2 1  1 2 3  4 3 2 1  1 2 3 4 5

---

(1 + n) * n / 2 = k





'''
number = int(input())

count = 1

if number == 1:
    print('1/1')
else:
        
    while(True):
        if (1 + count) * count / 2 < number:
            count += 1
        else :
            break
    
    number_check = count * (count - 1) / 2
    case_1 = int(number - number_check)
    case_2 = int(count - case_1 + 1)

    
    if (count % 2) == 0:
        print(str(case_1) + '/' + str(case_2))
    else:
        print(str(case_2) + '/' + str(case_1))