import os

dir_path = os.path.dirname( os.path.abspath( __file__ ) )
log_info = {}

def string_analyzer(log_string):
	log_string = log_string.replace('\n', '')
	log_list = []
	start_char_idx = 0
	end_char_idx = 0
	string_size = len(log_string)
	detail_start_idx = 0
	detail_end_idx = string_size

	for char_idx, char in enumerate(log_string):
		if char == '[':
			start_char_idx = char_idx+1
		
		if start_char_idx > 0 and char == ']':
			if char_idx == string_size-1:
				detail_start_idx = end_char_idx+1
				detail_end_idx = start_char_idx-1
				end_char_idx = char_idx
			else:
				end_char_idx = char_idx
				detail_start_idx = end_char_idx+1
				detail_end_idx = string_size
			
			log_element = log_string[start_char_idx:end_char_idx]
			log_list.append(log_element)
	
	log_element = split_detail_log(log_string[detail_start_idx:detail_end_idx].strip())
	log_list.append(log_element)
	save_to_log_info(log_list)

def split_detail_log(detail_log):
	split_point = detail_log.find(':')
	if split_point != -1:
		return (detail_log[:split_point], detail_log[split_point+1:])

	return ('ETC', detail_log[split_point+1:])

def save_to_log_info(log_list):
	global log_info
	log_detail = log_list.pop(-1)
	if log_list:
		log_time = log_list.pop(0)
		log_type = log_list.pop(0)
	
		if log_info.has_key(log_type): 
			if log_info[log_type].has_key(log_detail[0]):
				log_info[log_type][log_detail[0]] += 1 
			else:
				log_info = {log_type:{log_detail:1}}
		else:
			log_info = {log_type:{log_detail:1}}

def print_log_info(log_info):
	print '='*100
	for err_head in log_info['error']:
		print err_head
		for err_detail in log_info['error'][err_head]:
			print err_detail

def main():
	try :
		error_file = open('%s/error_log'%dir_path)

		for line in error_file.readlines():
			string_analyzer(line)

	except IOError:
		print 'Except IOError'

	print_log_info(log_info)

main()
