#exercise 0
def print_name(name):
	print 'your name is : %s'%name

#exercise 1
def print_rename(first_name, last_name):
	print_name(first_name)
	print 'he is from %s family'%last_name

#exercise 2
def return_abs(number):
	if number>0:
		return number
	else:
		return number*(-1)


#exercise 3
def addAddaDDaDd():
	user_num = raw_input()
	user_num = int(user_num)

	if user_num > 0 and user_num<10:
		return user_num+10
	elif user_num < 100:
		return user_num*0.1
	else:
		return False


#exercise 4
import math

def getDistance(x1, y1, x2, y2):
	return math.sqrt(((x2-x1)**2 + (y2-y1)**2))


#exercise 5
def getCharCount(string='next people', checkChar='e'):
	count = 0
	for c in string:
		if c==checkChar:
			count += 1
	return count


#exercise 6
def checkReverseString(string):
	for c in range(len(string)/2):
		if string[c] == string[-(c+1)]:
			pass
		else:
			return 'different'
		
	return 'same'

print 'exercise_6__TEST'
assert checkReverseString('abba') == 'same'
assert checkReverseString('abcdfe') == 'different'
assert checkReverseString('abcdcba') == 'same'
print '...   Text Success'

