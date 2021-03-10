# Tổng và tích của 3 số đó
# In ra số lớn nhất
# In ra số nhỏ nhất
# Phép chia lấy phần nguyên, phần dư và kết quả chính xác của hai số bất kỳ trong 3 số đó.

# Moi ban nhap:
# So a: 1
# So b: 2
# So c: 3

# Tong cua 3 so la: 6
# Số lớn nhất: 3
# Số nhỏ nhất: 1
# Chia lấy nguyên của 1 và 3 là: 0
# Chia lấy dư của 1 và 3 là: 2

print('Moi ban nhap:')
a = int(input('So a: '))
b = int(input('So b: '))
c = int(input('So c: '))

sum = a + b + c

print('Tong cua 3 so la: {0}'.format(sum))

max = a
if b > a:
    max = b

if c > max:
    max = c


print('Số lớn nhất: {0}'.format(max))
print('Chia lấy nguyên của {0} và {1} là : {2}'.format(a, c, a//c))
print('Chia lấy nguyên của {0} và {1} là : {2}'.format(a, c, a%c))


# Số lớn nhất: 3
# Số nhỏ nhất: 1
# Chia lấy nguyên của 1 và 3 là: 0
# Chia lấy dư của 1 và 3 là: 2