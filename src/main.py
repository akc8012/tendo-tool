import os

script_path = os.path.dirname(__file__)
template_path = '../assets/template.md'

path = os.path.join(script_path, template_path)

front_matter = {}
dash_line_count = 0

with open(path) as file:
	for line in file:
		line = line.strip()
		if line == '---':
			dash_line_count += 1
			if dash_line_count == 1:
				continue
			elif dash_line_count == 2:
				break

		key, value = line.split(':')
		key = key.strip()
		value = value.strip()

		front_matter[key] = value

# print(front_matter)

output = open(os.path.join(script_path, '../out/extremee.md'), 'a')
output.write('dank')
output.close()
