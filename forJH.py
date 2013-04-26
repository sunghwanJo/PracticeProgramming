#exercise 0
def print2(name):
	print 'your name is : %s'%name

print2('JiHwan')

#exercise 1
def print_rename(first_name, last_name):
	print(first_name)
	print 'he is from %s family'%last_name

print_rename('Jihwan', 'Kim')

#exercise 2
def return_abs(number):
	if number>0:
		return number
	else:
		return number*(-1)

print return_abs(3)
print return_abs(-4)


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

