a = float(input('Nhập điểm: '))

if a < 4 :
    print('F')
elif a >= 4 and a < 5 :
    print('D')
elif a >= 5 and a < 5.5 :
    print('D+')
elif a >= 5.5 and a < 6.5 :
    print('C')
elif a >= 6.5 and a < 7 :
    print('C+')
elif a >= 7 and a < 8 :
    print('B')
elif a >= 8 and a < 8.5 :
    print('B+')
elif a >= 8.5 and a < 9 :
    print('A')
else:
    print('A+')
