import yaml
import sys

def format_languages(langs):
    if not langs:
        return ''
    out = 'languages:\n  title: Languages\n  info:\n'
    for lang in langs:
        out += f'    - idiom: {lang["idiom"]}\n      level: {lang["level"]}\n'
    return out

def format_interests(interests):
    if not interests:
        return ''
    out = 'interests:\n  title: Interests\n  info:\n'
    for item in interests:
        out += f'    - item: {item["item"]}\n'
        if item.get("link"):
            out += f'      link: {item["link"]}\n'
    return out

def format_skills(skills):
    out = 'skills:\n  title: Skills\n  toolset:\n'
    for tool in skills['toolset']:
        # Output as a comma-separated list
        out += f'    - name: {tool["name"]}\n    - list: {", ".join(tool["list"])}\n'
    return out

def format_publications(publications):
    out = 'publications:\n  title: Publications\n  papers:\n'
    for paper in publications['papers']:
        # Highlight "Michael Wilkins" in authors
        authors = paper['authors'].replace('Michael Wilkins', '<strong>Michael Wilkins</strong>')
        out += f'    - title: "{paper["title"]}"\n'
        out += f'      link: "{paper["link"]}"\n'
        out += f'      authors: {authors}\n'
        out += f'      conference: {paper["conference"]}\n'
    return out

def format_projects(projects):
    out = f'projects:\n  title: {projects["title"]}\n  intro: >\n    {projects["intro"].strip()}\n  info:\n'
    for proj in projects['info']:
        out += f'    - role: {proj["role"]}\n'
        out += f'      time: {proj["time"]}\n'
        out += f'      details: |\n'
        for detail in proj['details']:
            out += f'        - {detail}\n'
    return out

def format_experiences(experiences):
    out = f'experiences:\n  title: {experiences["title"]}\n  info:\n'
    for exp in experiences['info']:
        out += f'    - role: {exp["role"]}\n'
        out += f'      time: {exp["time"]}\n'
        out += f'      company: {exp["company"]}\n'
        out += f'      details: |\n'
        for detail in exp['details']:
            out += f'        - {detail}\n'
    return out

def format_education(education):
    out = f'education:\n  title: {education["title"]}\n  info:\n'
    for ed in education['info']:
        out += f'    - degree: {ed["degree"]}\n'
        out += f'      university: {ed["university"]}\n'
        out += f'      time: {ed["time"]}\n'
    return out

def main():
    if len(sys.argv) != 3:
        print("Usage: python generate_website_yaml.py input_clean.yaml output_website.yaml")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r') as f:
        data = yaml.safe_load(f)

    # Start building the output YAML as a string
    out = ''

    # Sidebar
    out += '# # Be aware that even a small syntax error here can lead to failures in output.\n'
    out += 'sidebar:\n'
    out += f'  position: {data["sidebar"]["position"]}\n'
    out += f'  # position of the sidebar : left or right\n'
    out += f'  about: {str(data["sidebar"]["about"])}\n'
    out += f'  # set to False or comment line if you want to remove the "how to use?" in the sidebar\n'
    out += f'  education: {str(data["sidebar"]["education"])}\n'
    out += f'  # set to False if you want education in main section instead of in sidebar\n'

    # Profile
    out += '  # Profile information\n'
    out += f'  name: {data["profile"]["name"]}\n'
    out += f'  tagline: {data["profile"]["tagline"]}\n'
    out += f'  avatar: {data["profile"]["avatar"]}\n'
    out += '  #place a 100x100 picture inside /assets/images/ folder and provide the name of the file below\n'

    # Sidebar links
    out += '# Sidebar links\n'
    for k, v in data['contacts'].items():
        out += f'{k}: {v}\n'

    # Career profile
    out += 'career-profile:\n'
    out += f'  title: {data["career_profile"]["title"]}\n'
    out += f'  summary: |\n'
    for line in data["career_profile"]["summary"].split('\n'):
        out += f'    {line}\n'

    # Education
    out += format_education(data['education'])

    # Experiences
    out += format_experiences(data['experiences'])

    # Projects
    out += format_projects(data['projects'])

    # Publications
    out += format_publications(data['publications'])

    # Skills
    out += format_skills(data['skills'])

    # Footer
    out += f'footer: >\n  Credit to <a href="http://themes.3rdwavemedia.com" target="_blank" rel="nofollow">Xiaoying Riley</a> for the base webpage template\n'

    # Write to output file
    with open(output_file, 'w') as f:
        f.write(out)

    print(f"Website YAML generated at {output_file}")

if __name__ == "__main__":
    main()