import json

from jinja2 import Environment, FileSystemLoader, select_autoescape

# BASE = "https://pylondinium.org/"
BASE = "http://localhost:8000/"
PAGES = ["index.html", "keynote.html", "venue.html", "coc.html"]

env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape(["html", "xml"]))

for page in PAGES:
    template = env.get_template(page)
    with open(page, "w") as fo:
        fo.write(template.render(base=BASE))

template = env.get_template("schedule.html")

with open("talks.json") as fo:
    talks = json.load(fo)

with open("schedule.html", "w") as fo:
    fo.write(template.render(base=BASE, talks=talks))

template = env.get_template("talk.html")

for i, t in enumerate(talks):
    with open(f"talks/talk-{i}.html", "w") as fo:
        fo.write(template.render(base=BASE, talk=t))
