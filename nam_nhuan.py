year = int(input('Nhập năm để kiểm tra:'))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
	if (year > 2000):
		print('{0} là lớn hơn 2000'.format(year))
	else: 
		print('{0} là nhỏ hơn 2000'.format(year))
	print('{0} là năm nhuận'.format(year))
else:
	print('{0} không là năm nhuận'.format(year))
