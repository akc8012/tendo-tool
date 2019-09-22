import os

script_path = os.path.dirname(__file__)
template_path = "../assets/template.md"

path = os.path.join(script_path, template_path)
file = open(path)

print(file.read())
