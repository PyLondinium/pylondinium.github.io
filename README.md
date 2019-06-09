# pylondinium.org

Source code for [pylondinium.org](https://pylondinium.org/).

## Building

The website is generated from the 1) the templates in the `templates` directory and 2) the talk info in `talks.json`. The generated output is kept in the same tree as the templates to keep the `git`-fu as simple as humanly possible, whilst making edits easier.

To install development dependencies, execute the following command inside a `virtualenv`:

    pip install -r requirements.txt

To regenerate the website, just run `python3.7 generate.py`; optionally, you can pass in a `--base` argument that changes the base URL. For example, I set it to `http://localhost:8000/` for local development and `https://alexchamberlain.github.io/pylondinium.github.io/` to post a demo. You'll need `jinja2` and `markdown` installed, because they're just too awesome not to use; I use a `virtualenv`.
