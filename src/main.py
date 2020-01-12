import os

class FrontMatter:
	def read_template(self):
		script_path = os.path.dirname(__file__)
		template_path = '../assets/template.md'

		path = os.path.join(script_path, template_path)

		with open(path) as f:
			return f.read().splitlines()

	def go(self, file):
		front_matter = {}
		dash_line_count = 0

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

		return front_matter


front_matter = FrontMatter()
file = front_matter.read_template()
print(front_matter.go(file))
