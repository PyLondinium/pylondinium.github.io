import json

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape(["html", "xml"]))

template = env.get_template("schedule.html")

with open("talks.json") as fo:
    talks = json.load(fo)

with open("schedule.html", "w") as fo:
    fo.write(template.render(talks=talks))

template = env.get_template("talk.html")

for i, t in enumerate(talks):
    with open(f"talks/talk-{i}.html", "w") as fo:
        fo.write(template.render(talk=t))
