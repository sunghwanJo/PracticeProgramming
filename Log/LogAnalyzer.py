import os
import re

class LogAnalyzer():
	
	def __init__(self, log_file='Dont Exist File'):
		self.log_file = log_file
		self.log_info = {}

	def set_log_file(self, log_file):
		self.log_file = log_file

	def make_error_log(self):
		for line in self.read_file(self.log_file):
		
			if not self.filter_image_file(line) and'[error]' in line:
				err_set = line.split(']')[-1].strip().split(':', 1)
				
				if len(err_set) < 2:
					err_set.append(' ')
				self.add_log_info(err_set)

	def filter_image_file(self, log_string):
		image_pattern = re.compile(r'\w+.(jpg|gif|png)')
		try:
			re.search(image_pattern, log_string).group()
			return True
		except:
			return False

	def add_log_info(self, err_set):
		if err_set[0] in self.log_info:
			self.log_info[err_set[0]]['num'] += 1
			if not err_set[1] in self.log_info[err_set[0]]['errors']:
				self.log_info[err_set[0]]['errors'].append(err_set[1])
		else:
			self.log_info[err_set[0]] = {'num':1, 'errors': [err_set[1]]}
			
	def read_file(self, log_file):
		try:
			log_file = open(log_file)
		except IOError:
			print 'IOError'
		except:
			print 'IDonKnow'
		return log_file

	def make_report(self):
		dir_path = os.path.dirname( os.path.abspath( __file__ ) )
		with open(dir_path+'/report.sh', 'w') as report_file:
			report_file.write()

	def print_log_info(self):
		print self.log_info

	def __del__(self):
		pass

	def __repr__(self):
		return 'Processing '+self.log_file

a = LogAnalyzer('error_log')
a.make_error_log()
a.print_log_info()

#a.make_report()
