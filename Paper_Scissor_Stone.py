import random
com = random.choice(['布', '剪刀', '石頭'])
while True:
	player = input ('剪刀石頭布，請出拳：')
	if player != '布' and player != '剪刀' and player != '石頭':
		print ('請輸入 剪刀/石頭/布 唷')
		continue
	else:
		break
print ('我出的是', com)
if player == com:
	print ('平手!')
elif (player == '布' and com == '石頭') or (player == '剪刀' and com == '布') or ( player == '石頭' and com == '剪刀'):
	print ('恭喜你贏啦!')
else:
	print ('真可惜~再接再厲吧!')