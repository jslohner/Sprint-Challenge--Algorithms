'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
	# initialize count variable
	count = 0
	# check if string has more than one character
	if len(word) > 1:
		# if first letter of str is 't'
		if word[0] == 't':
			# if second letter of str is 'h'
			if word[1] == 'h':
				# add 1 to the count and add the return
				# of the recursive call to count_th()
				count += 1
				count += count_th(word[1:])
			# if second letter of str isn't 'h' add the
			# return of the call to count_th() to count
			else:
				count += count_th(word[1:])
		# if first letter of str isn't 't' add the
		# return of the call to count_th() to count
		else:
			count += count_th(word[1:])
	# return count
	return count
