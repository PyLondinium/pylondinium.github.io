import argparse
import json
import os

from jinja2 import Environment, FileSystemLoader, select_autoescape, Markup
import markdown

dir_path = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser(description="Generate pylondinium.org website.")
parser.add_argument("--base", default="https://pylondinium.org/", help="Base URL")

args = parser.parse_args()

PAGES = ["index.html", "keynote.html", "venue.html", "coc.html", "index-20190511.css"]

md = markdown.Markdown()
env = Environment(
    loader=FileSystemLoader(os.path.join(dir_path, "templates")), autoescape=select_autoescape(["html", "xml"])
)
env.filters["markdown"] = lambda text: Markup(md.reset().convert(text))

for page in PAGES:
    template = env.get_template(page)
    with open(os.path.join(dir_path, page), "w") as fo:
        fo.write(template.render(base=args.base))

template = env.get_template("schedule.html")

with open(os.path.join(dir_path, "talks.json")) as fo:
    talks = json.load(fo)

with open(os.path.join(dir_path, "workshops.json")) as fo:
    workshops = json.load(fo)

with open(os.path.join(dir_path, "schedule.html"), "w") as fo:
    fo.write(template.render(base=args.base, talks=talks, workshops=workshops))

template = env.get_template("talk.html")

for i, t in enumerate(talks):
    with open(os.path.join(dir_path, f"talks/talk-{i}.html"), "w") as fo:
        fo.write(template.render(base=args.base, talk=t))

template = env.get_template("workshop.html")

for k, t in workshops.items():
    with open(os.path.join(dir_path, f"talks/{k}.html"), "w") as fo:
        fo.write(template.render(base=args.base, talk=t))
