print('Hello, welcome to the complete facts!')

ans = input('Are you ready to play? (yes/no): ')
score = 0
total_q = 4

if ans.lower() == 'yes':
	ans = input('1. what color is the sky? ')
	if ans.lower() == 'blue':
		score += 1
		print('Correct')
	else:
		print('Incorrect')

	ans = input('2. who am i? ')
	if ans.lower() == 'god':
		score += 1
		print('Correct')
	else:
		print('Incorrect')

	ans = input('3. who are you? ')
	if ans.lower() == 'human':
		score += 1
		print('Correct')
	else:
		print('Incorrect')

	ans = input('4. will you obey me? ')
	if ans.lower() == 'yes':
		score += 1
		print('Correct')
	else:
		print('Incorrect')

print('you got ' + str(score) + ' questions correct.')
mark = (score/total_q) * 100

print('mark:', str(mark) + '%')
print('goodbye.')