import os

script_path = os.path.dirname(__file__)
template_path = '../assets/template.md'

path = os.path.join(script_path, template_path)

dict = {}
count = 0
dash_line_count = 0

with open(path) as file:
	for line in file:
		if line.strip() == '---':
			dash_line_count += 1
			if dash_line_count == 1:
				continue
			elif dash_line_count == 2:
				break

		if count == 0:
			dict[line.strip()] = 'default'
		else:
			dict[line.strip()] = ''

		# print(line)
		count += 1

print(dict)
