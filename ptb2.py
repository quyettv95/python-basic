print('Moi ban nhap:')
a = int(input('So a: '))
b = int(input('So b: '))
c = int(input('So c: '))

delta = b * b - 4 * a * c

if delta < 0:
    print('Phương trình vô nghiệm')
else:
    if delta == 0:
        print('Phương trình có nghiệm kép')
    else:
        print('Phương trình có 2 nghiệm')

if delta < 0:
    print('Phương trình vô nghiệm')
elif delta == 0:
    print('Phương trình có nghiệm kép')
else:
    print('Phương trình có 2 nghiệm')