'''#1
def del_list(list):
	del list[0]

letter = ['a', 'b', 'c']

print 'before_list'
print letter
del_list(letter)
print letter

#2
def dict_loop(dict):
	for name in dict:
		print name, dict[name]

sunghwan_info = {'name':'sunghwan', 'age':20}
dict_loop(sunghwan_info)

'''

#exercise 1

data = {'minsu':43, 'jisu':33, 'john':21, 'david':33, 'hary':36, 'messi':33, 'ronaldo':27}

def classifyAge(value):

	age_str = '%d0s'%(value/10)

	return age_str

def makeDict(makedDict):
	makeDict = {}

	for key in makedDict.keys():
		ages = classifyAge(makedDict[key])

		if makeDict.has_key(ages):
			makeDict[ages].append(key)
		else:
			makeDict[ages] = [key]

	return makeDict

print makeDict(data)
