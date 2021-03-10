a = int(input('Nhập năm: '))

canIndex = a % 10
canStr = ''

if canIndex == 0:
    canStr = 'Canh'
if canIndex == 1:
    canStr = 'Tân'
if canIndex == 2:
    canStr = 'Nhâm'
if canIndex == 3:
    canStr = 'Quý'
if canIndex == 4:
    canStr = 'Giáp'
if canIndex == 5:
    canStr = 'Ất'
if canIndex == 6:
    canStr = 'Bính'
if canIndex == 7:
    canStr = 'Đinh'
if canIndex == 8:
    canStr = 'Mậu'
if canIndex == 9:
    canStr = 'Kỷ'


chiIndex = (a % 100 ) % 12
chiStr = ''
if chiIndex == 0:
    chiStr = 'Tý'
if chiIndex == 1:
    chiStr = 'Sửu'
if chiIndex == 2:
    chiStr = 'Dần'
if chiIndex == 3:
    chiStr = 'Mão'
if chiIndex == 4:
    chiStr = 'Thìn'
if chiIndex == 5:
    chiStr = 'Tỵ'
if chiIndex == 6:
    chiStr = 'Ngọ'
if chiIndex == 7:
    chiStr = 'Mùi'
if chiIndex == 8:
    chiStr = 'Thân'
if chiIndex == 9:
    chiStr = 'Dậu'
if chiIndex == 10:
    chiStr = 'Tuất'
if chiIndex == 11:
    chiStr = 'Hợi'

print('Năm âm lịch của bạn là {0} {1}'.format(canStr, chiStr))
