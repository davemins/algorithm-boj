"""벌집"""

'''
1  -> 1개
7  -> 2개  1+6  : 1+6  :6*1
19 -> 3개 7+12  : 1+18 :6*3
37 -> 4개 19+18 : 1+36 :6*6
61 -> 5개 37+24 : 1+60 :6*10


1 -> 1개 : 1
2 -> 2개 : 1+1
8 -> 3개 : 2+6
20 -> 4개 : 8+12
38 -> 5개


    '''
while 1:
    number = int(input())

    def door(num):
        if num == 1:
            return 1
        else:
            door_num = 0
            while True:
                if num < 2 + 3 * (door_num * (door_num - 1)):
                    break
                door_num += 1
            return door_num

    print(door(number))
    print()
