import argparse
import json

from jinja2 import Environment, FileSystemLoader, select_autoescape, Markup
import markdown

parser = argparse.ArgumentParser(description="Generate pylondinium.org website.")
parser.add_argument("--base", default="https://pylondinium.org/", help="Base URL")

args = parser.parse_args()

PAGES = ["index.html", "keynote.html", "venue.html", "coc.html", "index-20190511.css"]

md = markdown.Markdown()
env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape(["html", "xml"]))
env.filters["markdown"] = lambda text: Markup(md.reset().convert(text))

for page in PAGES:
    template = env.get_template(page)
    with open(page, "w") as fo:
        fo.write(template.render(base=args.base))

template = env.get_template("schedule.html")

with open("talks.json") as fo:
    talks = json.load(fo)

with open("schedule.html", "w") as fo:
    fo.write(template.render(base=args.base, talks=talks))

template = env.get_template("talk.html")

for i, t in enumerate(talks):
    with open(f"talks/talk-{i}.html", "w") as fo:
        fo.write(template.render(base=args.base, talk=t))
