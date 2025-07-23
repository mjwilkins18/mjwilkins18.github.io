import yaml
from jinja2 import Template

# Load YAML file
with open("../_data/raw_data.yml", "r") as file:
    data = yaml.safe_load(file)

# Load LaTeX template
with open("resume_template.tex", "r") as file:
    template = Template(file.read(), trim_blocks=True, lstrip_blocks=True)

# Render LaTeX document
latex_output = template.render(data)

# Save rendered LaTeX to a file
with open("resume.tex", "w") as file:
    file.write(latex_output)

print("LaTeX file generated: resume.tex")
